# Flow.Launcher.Plugin.PeriodicTable

This is a plugin for Flow Launcher to get key characteristics of an element in the periodic table by the symbol name.
It uses the periodictable library to get the information.

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

- [x] Element lookup is too slow. Find a way to speed it up
- [ ] Add more information about the element

#

P.S. This is my frist real contribution to an open source project. I hope you like it. If you have any suggestions or
improvements, please let me know.
Plugin icon from: [https://www.flaticon.com/free-icons/periodic-table](https://www.flaticon.com/free-icons/periodic-table)
