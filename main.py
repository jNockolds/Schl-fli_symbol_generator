from numpy import gcd

def get_var_name(var) -> str:
    for name, value in globals().items():
        if value is var:
            return name

def print_schlafli(schlafli : tuple, end='\n'):
    print('{' + f"{schlafli[0]}/{schlafli[1]}" + '}', end=end)

def print_list(input : list) -> None:
    print(f"\n{get_var_name(input)}:") # list name
    [print_schlafli(x, end= ", ") for x in input[0:len(input)]] # list contents
    print_schlafli(input[-1]) # list contents


non_degenerates : list[tuple] = []
degenerates : list[tuple] = []

def generate_polygon_lists(non_degenerates : list, degenerates : list, max_sides : int, max_density=None) -> None:
    if max_density == None:
        max_density = max_sides // 2
    elif max_density > max_sides // 2:
        raise ValueError("requirement: max_density <= max_sides // 2")
    
    for density in range(1, max_density + 1):
        for sides in range(1, max_sides + 1):
            if gcd(sides, density) != 1:
                degenerates.append((sides, density))
            else:
                non_degenerates.append((sides, density))

generate_polygon_lists(non_degenerates, degenerates, 12)

print_list(non_degenerates)
print_list(degenerates)
print()
