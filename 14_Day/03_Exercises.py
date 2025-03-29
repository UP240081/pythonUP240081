from collections import Counter
from countries_data import countries_d

# Sorting functions
sorted_by_name = sorted(countries_d, key=lambda x: x["name"])
sorted_by_capital = sorted(countries_d, key=lambda x: x["capital"])
sorted_by_population = sorted(countries_d, key=lambda x: x["population"], reverse=True)

# Top 10 most populated countries
top_10_populated_countries = sorted_by_population[:10]

# Counting occurrences of each language
language_counts = {}
for country in countries_d:
    for language in country["languages"]:
        language_counts[language] = language_counts.get(language, 0) + 1

# Top 10 most spoken languages
top_10_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Display results
print("Countries sorted by name:", [c["name"] for c in sorted_by_name])
print("Countries sorted by capital:", [c["capital"] for c in sorted_by_capital])
print("Countries sorted by population:", [(c["name"], c["population"]) for c in sorted_by_population])
print("Top 10 most populated countries:", [(c["name"], c["population"]) for c in top_10_populated_countries])
print("Top 10 most spoken languages:", top_10_languages)
