# Flow.Launcher.Plugin.PeriodicTable

This is a plugin for Flow Launcher to get key characteristics of an element in the periodic table by the symbol name.
It uses a json file (by Bowserinator, see below) to get the information. If some data is incorrect, please create a new
issue. So the error can be fixed.
## Usage

The default keyword is `pt`. You can use the following command to get the information of an element.

```shell
pt <element symbol>
```

This will return the following information:

- Name
- Symbol
- Atomic Number
- Atomic Mass

Also note that the symbol is case-sensitive so `pt h` won't work but `pt H` will.

## Possible future improvements

- [x] Element lookup is too slow. Find a way to speed it up.
- [x] Add more information about the element.
- [ ] Make improvements based on user feedback if there is any.

## Thanks to

- Bowserinator for maintaining the repository of the periodictable JSON file. You can find
  it [here](https://github.com/Bowserinator/Periodic-Table-JSON/blob/master/PeriodicTableJSON.json).
- flaticon, where the plugin icon comes from.[flaticon](https://www.flaticon.com/free-icons/periodic-table)

P.S. This is my first real contribution to an open source project. I hope you like it. If you have any suggestions or
improvements, please let me know.


