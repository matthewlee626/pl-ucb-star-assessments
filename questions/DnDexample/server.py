import io


def generate(data):

    # Generate complete html string
    mytable = '''
        <table id="data-frame">
        <thead>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
                <th>Column 3</th>
                <th>Column 4</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Row 1</td>
                <td>Row 1</td>
                <td>Row 1</td>
                <td>Row 1</td>
            </tr>
            <tr>
                <td>Row 2</td>
                <td>Row 2</td>
                <td>Row 2</td>
                <td>Row 2</td>
            </tr>
            <tr>
                <td>Row 3</td>
                <td>Row 3</td>
                <td>Row 3</td>
                <td>Row 3</td>
            </tr>
        </tbody>
    </table>'''
    data["params"]["mytable"] = mytable

