import re

def convert_mysql_to_sqlite(mysql_dump, sqlite_dump):
    with open(mysql_dump, 'r') as infile, open(sqlite_dump, 'w') as outfile:
        for line in infile:
            # Remove USE statements
            if line.strip().upper().startswith('USE'):
                continue
            
            # Remove MySQL-specific index lengths
            line = re.sub(r'\(\d+\)', '', line)
            
            # Replace ` with "
            line = line.replace('`', '"')
            
            # Replace AUTO_INCREMENT with AUTOINCREMENT
            line = line.replace('AUTO_INCREMENT', 'AUTOINCREMENT')
            
            # Remove MySQL-specific ENGINE statements
            line = re.sub(r'ENGINE=\w+\s*', '', line)
            
            # Remove CHARACTER SET statements
            line = re.sub(r'CHARACTER SET \w+\s*', '', line)
            
            # Remove COLLATE statements
            line = re.sub(r'COLLATE \w+\s*', '', line)
            
            # Replace int(11) with INTEGER
            line = re.sub(r'\bint\(\d+\)', 'INTEGER', line, flags=re.IGNORECASE)
            
            # Replace tinyint(1) with BOOLEAN
            line = re.sub(r'\btinyint\(1\)', 'BOOLEAN', line, flags=re.IGNORECASE)
            
            # Replace double with REAL
            line = re.sub(r'\bdouble\b', 'REAL', line, flags=re.IGNORECASE)
            
            # Replace datetime with TEXT (SQLite does not have a native datetime type)
            line = re.sub(r'\bdatetime\b', 'TEXT', line, flags=re.IGNORECASE)
            
            # Replace enum with TEXT (SQLite does not have a native enum type)
            line = re.sub(r'\benum\([^)]+\)', 'TEXT', line, flags=re.IGNORECASE)
            
            # Write the modified line to the output file
            outfile.write(line)

# Usage
convert_mysql_to_sqlite('sql/Waoflix_DJ.sql', 'sqlite_dump.sql')