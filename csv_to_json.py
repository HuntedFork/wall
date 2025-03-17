#!/usr/bin/env python3
import json
import sys

def robust_parse_player_game(line):
    """
    Parses a line representing a player game.
    The expected format is something like:
      [[chat1,chat2,...],[chat1,chat2,...], ...]
    However, the data may contain invalid characters (e.g., stray parentheses)
    which this parser will ignore if possible.
    
    This parser:
      - Removes an outer pair of square brackets if they exist.
      - Scans the line character‑by‑character for subarrays (delimited by '[' and ']').
      - Splits the content of each subarray on commas.
    
    Note: If a subarray is malformed, it will be skipped.
    """
    line = line.strip()
    # Remove the outer brackets if they exist.
    if line.startswith('[') and line.endswith(']'):
        line = line[1:-1]
    
    player_game = []
    i = 0
    n = len(line)
    
    while i < n:
        # Skip whitespace and commas.
        while i < n and (line[i].isspace() or line[i] == ','):
            i += 1
        if i < n and line[i] == '[':
            start = i + 1
            j = line.find(']', start)
            if j == -1:
                # If no closing bracket is found, break out.
                break
            subarray_str = line[start:j]
            # Split on commas; strip extra whitespace.
            tokens = [token.strip() for token in subarray_str.split(',') if token.strip() != '']
            player_game.append(tokens)
            i = j + 1
        else:
            # Advance if not an opening bracket.
            i += 1
    return player_game

def convert_txt_to_js(input_path, output_path=None, max_lines=None):
    all_games = []
    with open(input_path, 'r', encoding='utf-8') as infile:
        for line_no, line in enumerate(infile):
            if max_lines is not None and line_no >= max_lines:
                break
            line = line.strip()
            if not line:
                continue  # Skip empty lines.
            try:
                player_game = robust_parse_player_game(line)
                all_games.append(player_game)
            except Exception as e:
                print(f"Error parsing line: {line}\n{e}")
                continue
    
    # Convert the nested structure to a pretty-printed JSON string.
    js_array = json.dumps(all_games, indent=2)
    js_content = f"let data = {js_array};"
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(js_content)
        print(f"JavaScript variable file written to {output_path}")
    else:
        print(js_content)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt [output.js] [maxLines]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    max_lines = None

    # Determine the optional arguments.
    # If there's a second argument, check if it's numeric (maxLines) or an output file.
    if len(sys.argv) >= 3:
        try:
            # Try converting the second argument to an integer.
            max_lines = int(sys.argv[2])
        except ValueError:
            # If not numeric, it's the output file.
            output_file = sys.argv[2]
    # If there's a third argument, it must be maxLines.
    if len(sys.argv) == 4:
        try:
            max_lines = int(sys.argv[3])
        except ValueError:
            print("maxLines must be an integer.")
            sys.exit(1)
    
    convert_txt_to_js(input_file, output_file, max_lines)
