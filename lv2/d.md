```python
import dis
import marshal

with open("chall.pyc", "rb") as f:
    f.seek(16)
    print(dis.dis(marshal.load(f)))

```

https://blog.hamayanhamayan.com/entry/2023/09/11/071621#forensics-Barbara-Liskov

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('CQAWB~v^kVi?bRl? bfLdLb_(wEk/ox/rLcMG@[')
              STORE_NAME               0 (flag_enc)

  3           LOAD_CONST               1 ('')
              STORE_NAME               1 (flag)

  5           LOAD_NAME                2 (range)
              PUSH_NULL
              LOAD_CONST               2 (0)
              LOAD_NAME                3 (len)
              PUSH_NULL
              LOAD_NAME                0 (flag_enc)
              CALL                     1
              CALL                     2
              GET_ITER
      L1:     FOR_ITER                26 (to L2)
              STORE_NAME               4 (i)

  6           LOAD_NAME                1 (flag)
              LOAD_NAME                5 (chr)
              PUSH_NULL
              LOAD_NAME                6 (ord)
              PUSH_NULL
              LOAD_NAME                0 (flag_enc)
              LOAD_NAME                4 (i)
              BINARY_SUBSCR
              CALL                     1
              LOAD_NAME                4 (i)
              BINARY_OP               12 (^)
              CALL                     1
              BINARY_OP               13 (+=)
              STORE_NAME               1 (flag)
              JUMP_BACKWARD           28 (to L1)

  5   L2:     END_FOR
              POP_TOP

  8           LOAD_NAME                7 (input)
              PUSH_NULL
              LOAD_CONST               3 ('Enter flag: ')
              CALL                     1
              STORE_NAME               8 (inp)

  9           LOAD_NAME                8 (inp)
              LOAD_NAME                1 (flag)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        9 (to L3)

 10           LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               4 ('Wrong!')
              CALL                     1
              POP_TOP
              RETURN_CONST             8 (None)

 12   L3:     LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               5 ('Correct!')
              CALL                     1
              POP_TOP

 13           LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               6 ('Flag: ')
              LOAD_CONST               1 ('')
              LOAD_CONST               7 (('end',))
              CALL_KW                  2
              POP_TOP
              RETURN_CONST             8 (None)
None
```

これをよしなにすると

```python
flag_enc = "CQAWB~v^kVi?bRl? bfLdLb_(wEk/ox/rLcMG@["
flag = "".join(chr(ord(c) ^ i) for i, c in enumerate(flag_enc))
print(flag)
```
