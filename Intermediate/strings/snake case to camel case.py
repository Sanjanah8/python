def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Example usage:
print(snake_to_camel("hello_world_example"))  # Output: "helloWorldExample"
