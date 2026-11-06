
# Countries included in the analysis
COUNTRIES = ["Brazil", "India", "Afghanistan", "Mexico", "Canada"]

# Map lowercase filenames to country names in the dataset
COUNTRY_NAMES = {
    country.lower(): country
    for country in COUNTRIES
}


# Define the final outputs of the workflow
rule all:
    input:
        expand(
            "results/{country}.png",
            country=COUNTRY_NAMES.keys()
        )


# Generate a scatterplot for each country
rule plot_country:
    input:
        co2="data/Agrofood_co2_emission.csv",
        gdp="data/IMF_GDP.csv"
    output:
        "results/{country}.png"
    params:
        country=lambda wildcards: COUNTRY_NAMES[wildcards.country]
    shell:
        """
        python src/plot_fire_gdp.py \
            --co2 {input.co2} \
            --gdp {input.gdp} \
            --country {params.country} \
            --out {output}
        """
