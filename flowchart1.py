from graphviz import Digraph

dot = Digraph(format="png")
dot.attr(rankdir="LR")
dot.attr("node", shape="box", style="filled", fontsize="12")

dot.attr("node", fillcolor="#FFCC99")
dot.node("1", "Data Collection")
dot.node("2", "Web Scraping")
dot.node("3", "Data Wrangling")
dot.node("4", "EDA SQL")
dot.node("5", "EDA Plots")
dot.node("6", "EDA Folium")
dot.node("7", "Machine Learning")

dot.attr("node", fillcolor="#FFCCCC")
dot.node("Dash", "Interactive Dashboard")

dot.attr("node", fillcolor="#99CCFF")
dot.node("API", "SpaceX API\n(JSON)")
dot.node("Wiki", "Wikipedia\n(HTML)")

dot.attr("node", fillcolor="#99FF99")
dot.node("CSV1", "dataset_part_1.csv\n(CSV)")
dot.node("WebCSV", "spacex_web_scraped.csv\n(CSV)")
dot.node("CSV2", "dataset_part_2.csv\n(CSV)")
dot.node("CSV3", "dataset_part_3.csv\n(CSV)")
dot.node("SpaceXCSV", "Spacex.csv\n(CSV)")
dot.node("GeoCSV", "Spacex_launch_geo.csv\n(CSV)")
dot.node("DashCSV", "Spacex_launch_dash.csv\n(CSV)")

dot.edge("API", "1")
dot.edge("1", "CSV1")

dot.edge("Wiki", "2")
dot.edge("2", "WebCSV")

dot.edge("CSV1", "3")
dot.edge("3", "CSV2")
dot.edge("CSV2", "5")
dot.edge("5", "CSV3")

dot.edge("SpaceXCSV", "4")
dot.edge("GeoCSV", "6")

dot.edge("DashCSV", "Dash")

dot.edge("CSV2", "7")
dot.edge("CSV3", "7")

dot.render("jupyter_flowchart_updated", cleanup=True)

