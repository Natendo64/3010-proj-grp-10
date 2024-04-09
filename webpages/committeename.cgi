#!/usr/bin/python3
import cgi
import psycopg2

# Parse form data
form = cgi.FieldStorage()

# Extract search query and sort option from form
search_query = form.getvalue('search_query', '')
sort_option = form.getvalue('sort_option', 'id')

# Connect to the database
conn = psycopg2.connect(
    host="192.168.56.20",
    dbname="csdashboard",
    user="webuser1",
    password="student"
)

cursor = conn.cursor()

# Construct the SQL query based on search and sort options
sql_query = "SELECT * FROM committee_names"
if search_query:
    sql_query += f" WHERE lower(committee_name) LIKE lower('%{search_query}%')"
sql_query += f" ORDER BY {sort_option}"

cursor.execute(sql_query)
rows = cursor.fetchall()
cursor.close()
conn.close()

# Print HTTP header
print('Content-type: text/html\n\n')

#Quick Link Tabs
print("<html>")
print("<table>")
print("<tr>")
print("<td><a href='http://localhost/cgi-bin/faculty.cgi'>Faculty</a></td>")
print("<td><a href='http://localhost/cgi-bin/prerequisites.cgi'>Prerequisites</a></td>")
print("<td><a href='http://localhost/cgi-bin/courseschedulehistory.cgi'>Course Schedule History</a></td>")
print("<td><a href='http://localhost/cgi-bin/coursedirector.cgi'>Course Director</a></td>")
print("<td><a href='http://localhost/cgi-bin/committeeassignment.cgi'>Committee Assignment</a></td>")
print("</tr>")
print("</table>")
print("</html>")

# Print HTML response
print("<html>")
print("<head>")
print("<title>Committee Name Table</title>")
print("</head>")
print("<body>")
print("<h1>Committee Name Table</h1>")
print("<form method='get'>")
print("<label>Search:</label>")
print("<input type='text' name='search_query' value=''>")
print("<label>Sort By:</label>")
print("<select name='sort_option'>")
print("<option value='id'>ID</option>")
print("<option value='committee_name'>Committee Name</option>")
print("<option value='remarks'>Remarks</option>")
print("</select>")
print("<input type='submit' value='Submit'>")
print("</form>")
print("<table>")
print("<thead>")
print("<tr>")
print("<th>ID</th>")
print("<th>Committee Name</th>")
print("<th>Remarks</th>")
print("</tr>")
print("</thead>")
print("<tbody>")
for row in rows:
    print("<tr>")
    for value in row:
        print(f"<td>{value}</td>")
    print("</tr>")
print("</tbody>")
print("</table>")
print("</body>")
print("</html>")

