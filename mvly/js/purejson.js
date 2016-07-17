function render(jsonObject){
    var content = [
        {title: 'Json Resume', json: jsonObject}
    ];
    var result = document.querySelector('.json');
    content.forEach(function(example) {
        var title = document.createElement('h3');
        var formatter = new JSONFormatter(example.json, 1, example.config);
        title.innerText = example.title;
        result.appendChild(title)
        var el = formatter.render();
        result.appendChild(el);
    });
}