document.getElementById('readButton').addEventListener('click', function() {
    // Make an AJAX request to Flask route to generate text
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/generate_text', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            var generatedText = response.text;
            document.getElementById('displayText').textContent = generatedText;
        }
    };
    xhr.send();
});
