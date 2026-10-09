import argparse

import matplotlib.pyplot as plt

from fire_gdp import get_fire_gdp_year_data


plt.switch_backend("Agg")


def make_plot(co2_file, gdp_file, country, out_file):
    data = get_fire_gdp_year_data(
        co2_file,
        gdp_file,
        country
    )

    gdp = [row[2] for row in data]
    fires = [row[1] for row in data]

    fig, ax = plt.subplots()

    ax.scatter(gdp, fires)
    ax.set_xlabel("GDP")
    ax.set_ylabel("Forest fire emissions")
    ax.set_title(country)

    fig.savefig(out_file, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--co2", required=True)
    parser.add_argument("--gdp", required=True)
    parser.add_argument("--country", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    make_plot(
        args.co2,
        args.gdp,
        args.country,
        args.out
    )


if __name__ == "__main__":
    main()
