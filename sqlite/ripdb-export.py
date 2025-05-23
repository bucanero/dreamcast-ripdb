import sqlite3
import os

def export_rows_to_text_files(db_file, table_name, output_dir='output'):
    """
    Export each row from a SQLite table to individual text files.
    
    Args:
        db_file (str): Path to the SQLite database file
        table_name (str): Name of the table to export
        output_dir (str): Directory to save the text files (default: 'output')
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Get table information
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]
        
        # Get all rows from the table
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY UPPER(game_name)")
        rows = cursor.fetchall()
        
        mdi = open(os.path.join(output_dir, 'README.md'), 'w', encoding='utf-8')
        
        # Export each row to a separate file
        for i, row in enumerate(rows, start=1):
            fname = row[1].lower().replace(" ", "-").replace("/", "-").replace("*", "").replace(":", "").replace("?", "")
            filename = os.path.join(output_dir, f"{row[0]}-{fname}.md")
            
            mdi.write(f"- [{row[1]}]({row[0]}-{fname}.html)\r\n")
            
            with open(filename, 'w', encoding='utf-8') as f:
                # Write column headers and values
                for col, value in zip(columns, row):
                    if col == "game_name":
                        gname = value
                    elif col == "downsample":
                        dsam = value
                    elif col == "binhack":
                        bhack = value
                    elif col == "status":
                        status = value
                    elif col == "comments":
                        comments = value
                    elif col == "user_name":
                        usr = value
                    elif col == "date":
                        date = value

                f.write(f"# {gname}\r\n\r\n## Rip Details\r\n\r\n- **User:** {usr}\r\n- **Date:** {date}\r\n- **Status:** {status}\r\n\r\n## Downsampling\r\n\r\n{dsam}\r\n\r\n## Bin Hacking\r\n\r\n{bhack}\r\n\r\n## Comments\r\n\r\n{comments}\r\n\r\n")
            
            print(f"Exported row {i} to {filename}")
        
        print(f"\nSuccessfully exported {len(rows)} rows from table '{table_name}'")
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Example usage
    database_file = "ripdb.sqlite"  # Change to your database file
    table_to_export = "dc_ripdb"    # Change to your table name
    
    export_rows_to_text_files(database_file, table_to_export)
