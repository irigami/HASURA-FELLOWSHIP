# HASURA-FELLOWSHIP
prerequisites:
    python and flask installed on your system
running the code:
    get the code into a folder with python file and another folder named templates which contains all the remaining html files.run the python file using python3. For python 2 use the comment given at the start
    This will deploy a local server. According to the URL, it executes different functions: 'localhost:5000'+
    1.'/':displays Hello World - Prasanth
    2.'/authors':displays the list of the authors and the count of their posts by fetching the info from the url 'https://jsonplaceholder.typicode.com/users/' and its corresponding posts info url 'https://jsonplaceholder.typicode.com/posts/'
    3.'/setcookie':this will set cookies with names 'name' and 'age'
    4.'/getcookies':displays the stored cookie values along with names
    5.'/robots.txt':this displays that you are denied from accessing the url
    6.'/html': this renders the renderhtml.html file from the templates folder
    7.'/input': you will be asked to fill in a text input box which will be sent to '/display' endpoint which shows the value you typed along with displaying the value you typed in the stdout
