import networkx as nx
from recon.js_analyzer import extract_js_endpoints

def map_endpoints(pages):
    graph = nx.DiGraph()
    endpoints = set()

    for page in pages:
        graph.add_node(page)

        if "?" in page:
            endpoints.add(page)

        js_endpoints = extract_js_endpoints(page)

        for ep in js_endpoints:
            graph.add_edge(page, ep)
            endpoints.add(ep)

    return list(endpoints), graph
