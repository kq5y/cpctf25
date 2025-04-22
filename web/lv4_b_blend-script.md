ヒント２まで見たけど意味なかった。

Deno.readFile~でできなかったから違うだろうなと思ったけど調べたらできた。
https://qiita.com/access3151fq/items/48e17d1363de39d01ad1#%E6%96%B9%E6%B3%951%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEfetch

```js
const res = await fetch(new URL("/proc/self/environ", import.meta.url));
console.log(await res.text());
```
