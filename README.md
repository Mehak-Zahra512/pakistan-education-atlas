# Pakistan Education Atlas
An interactive map visualising education inequality
across Pakistan's provinces — built for researchers
and policymakers, not just data practitioners.

## The Problem
Education inequality in Pakistan is documented in reports
nobody reads. A map answers the same question in seconds.

## What I Built
An interactive province-level map covering 5 regions:
- Punjab
- Sindh
- KPK
- Balochistan
- Islamabad

Each province has a clickable marker showing:
- Literacy rate
- Internet access percentage
- Gender gap
- Out-of-school children percentage

## Key Design Choice
Circle marker radius scales to literacy rate —
inequality becomes visible before you read a single number.

## Output
An HTML file anyone can open in any browser.
No installation needed to view the results.

## Tech Stack
Python · Pandas · Folium · CSV Data Handling

## How to Run
pip install -r requirements.txt
python pakistan_education_atlas.py

## Honest Limitation
Dataset was manually compiled — not scraped from
a live government source yet.
Next version: connect to real-time UNESCO or
Pakistan Bureau of Statistics data.
