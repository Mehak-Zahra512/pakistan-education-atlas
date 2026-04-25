import pandas as pd
import folium

# Load data
df = pd.read_csv("pakistan_education.csv")

# Pakistan center map
pak_map = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

# Province coordinates (approx)
coords = {
    "Punjab": [31.1704, 72.7097],
    "Sindh": [25.8943, 68.5247],
    "KPK": [34.9526, 72.3311],
    "Balochistan": [28.4907, 65.0958],
    "Islamabad": [33.6844, 73.0479]
}

# Add markers
for _, row in df.iterrows():
    province = row["province"]

    if province in coords:
        lat, lon = coords[province]

        popup_text = f"""
        <b>{province}</b><br>
        Literacy Rate: {row['literacy_rate']}%<br>
        Out of School: {row['out_of_school']}%<br>
        Internet Access: {row['internet_access']}%<br>
        Gender Gap: {row['gender_gap']}%
        """

        folium.CircleMarker(
            location=[lat, lon],
            radius=row["literacy_rate"] / 5,
            popup=popup_text,
            fill=True
        ).add_to(pak_map)

# Save map
pak_map.save("education_map.html")

print("Map created successfully! Open education_map.html")