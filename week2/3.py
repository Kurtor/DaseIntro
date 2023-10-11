def find_all_paths(graph, start, end):
    paths = []
    stack = [(start, [start])]

    while stack:
        (node, path) = stack.pop()

        if node == end:
            paths.append(path)
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

    return paths

if __name__ == "__main__":
    my_graph = {
        "人-羊-狼-菜": {"狼-菜"},
        "狼-菜": {"人-狼-菜"},
        "人-狼-菜": {"狼", "菜"},
        "狼": {"人-羊-狼"},
        "菜": {"人-羊-菜"},
        "人-羊-狼": {"羊"},
        "人-羊-菜": {"羊"},
        "羊": {"人-羊"},
        "人-羊": {"成功"}
    }

    start_address = "人-羊-狼-菜"
    end_address = "成功"
    all_paths = find_all_paths(my_graph, start_address, end_address)
    for path in all_paths:
        print("->".join(path))
