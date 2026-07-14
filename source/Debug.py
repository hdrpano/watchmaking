from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def to_float(txt: str) -> float:
    return float(txt.strip().replace(",", "."))


def parse_belot_txt(path: str):
    points = []
    arcs = []
    header = {}

    for line in Path(path).read_text(encoding="latin-1").splitlines():
        parts = [p.strip() for p in line.split(";")]

        if len(parts) < 2:
            continue

        key = parts[0]

        if key in (
            "mobile",
            "Norme",
            "Module theo",
            "Module prat",
            "Diamètre de tête",
            "Diamètre primitif",
            "Diamètre générateur",
            "Diamètre de fond",
            "Cote XY",
            "Narc coté 1",
            "Narc total",
        ):
            header[key] = parts[1:]

        elif key == "point X-Y":
            points.append({
                "No": int(parts[1]),
                "X": to_float(parts[2]),
                "Y": to_float(parts[3]),
            })

        elif key == "arc R P Q Te Ts":
            arcs.append({
                "No": int(parts[1]),
                "R": to_float(parts[2]),
                "P": to_float(parts[3]),
                "Q": to_float(parts[4]),
                "Te": to_float(parts[5]),
                "Ts": to_float(parts[6]),
            })

    return header, points, arcs


def invert_profile_y(points, arcs):
    """
    Spiegelung an der Y-Achse.

    X  -> -X
    P  -> -P
    Te <-> Ts
    """

    new_points = []

    for p in points:
        new_points.append({
            "No": p["No"],
            "X": -p["X"],
            "Y": p["Y"],
        })

    new_arcs = []

    for a in arcs:
        new_arcs.append({
            "No": a["No"],
            "R": a["R"],
            "P": -a["P"],
            "Q": a["Q"],
            "Te": a["Ts"],
            "Ts": a["Te"],
        })

    return new_points, new_arcs


def plot_belot(points, arcs):

    fig, ax = plt.subplots(figsize=(8, 8))

    for i, arc in enumerate(arcs):

        p1 = points[i]
        p2 = points[i + 1]

        cx = arc["P"]
        cy = arc["Q"]

        r = abs(arc["R"])

        a1 = np.arctan2(
            p1["Y"] - cy,
            p1["X"] - cx,
        )

        a2 = np.arctan2(
            p2["Y"] - cy,
            p2["X"] - cx,
        )

        da = a2 - a1

        while da <= -np.pi:
            da += 2*np.pi

        while da > np.pi:
            da -= 2*np.pi

        t = np.linspace(a1, a1 + da, 200)

        x = cx + r*np.cos(t)
        y = cy + r*np.sin(t)

        ax.plot(x, y, "b")

    for p in points:

        ax.plot(
            p["X"],
            p["Y"],
            "ro",
        )

        ax.text(
            p["X"],
            p["Y"],
            str(p["No"]),
        )

    ax.set_aspect("equal")
    ax.grid(True)

    plt.show()


def print_belot_debug(path: str):
    header, points, arcs = parse_belot_txt(path)

    print("\n" + "=" * 80)
    print(path)
    print("=" * 80)

    print("\nHEADER")
    for k, v in header.items():
        print(f"{k:22s}: {' ; '.join(v)}")

    print("\nPOINTS")
    print(f"{'No':>3s} {'X':>14s} {'Y':>14s}")
    for p in points:
        print(f"{p['No']:3d} {p['X']:14.9f} {p['Y']:14.9f}")

    print("\nARCS")
    print(f"{'No':>3s} {'R':>14s} {'P':>14s} {'Q':>14s} {'Te':>14s} {'Ts':>14s}")
    for i in range(len(arcs)):

        arc = arcs[i]

        p1 = points[i]
        p2 = points[i + 1]

        r = abs(arc["R"])

        d1 = np.hypot(
            p1["X"] - arc["P"],
            p1["Y"] - arc["Q"],
        )

        d2 = np.hypot(
            p2["X"] - arc["P"],
            p2["Y"] - arc["Q"],
        )

        print(
            f"Arc {arc['No']:2d}  "
            f"r={r:.6f}  "
            f"d1-r={d1-r:+.6e}  "
            f"d2-r={d2-r:+.6e}"
        )


if __name__ == "__main__":

    File = "M28-CentralSec-asym_belot.txt"

    header, points, arcs = parse_belot_txt(
        File
    )

##    print_belot_debug(File)

##    print("\nARC TO ARC")
##
##    for i in range(len(arcs)):
##
##        a = arcs[i]
##        b = arcs[(i + 1) % len(arcs)]
##
##        xe = a["P"] + abs(a["R"]) * np.cos(a["Ts"])
##        ye = a["Q"] + abs(a["R"]) * np.sin(a["Ts"])
##
##        xs = b["P"] + abs(b["R"]) * np.cos(b["Te"])
##        ys = b["Q"] + abs(b["R"]) * np.sin(b["Te"])
##
##        gap = np.hypot(xe - xs, ye - ys)
##
##        print(
##            f"{a['No']:2d}->{b['No']:2d} "
##            f"gap={gap:.9e}"
##        )

    plot_belot(points, arcs)


    points, arcs = invert_profile_y(
        points,
        arcs,
    )

    plot_belot(points, arcs)
