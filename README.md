# Flow.Launcher.Plugin.PeriodicTable

> [!IMPORTANT]  
> Plugin now archived see note below.

> [!NOTE]
> I would recomend using [This](https://github.com/asmpro7/ElementFlow) plugin instead of mine because it has way more information.

This is a plugin for Flow Launcher to get key characteristics of an element in the periodic table.
It uses a json file (by Bowserinator, see below) to get the characteristics. If a characteristic is incorrect, please
create an
issue. So the error can be fixed.
## Usage

The default keyword is `pt`. You can use the following command to get the information of an element.

```shell
pt <element symbol or element name>
```

you can also use the full name of the element. For example:

```shell
pt Hydrogen
```

or you can use autocomplete and type the first few letters of the element name. For example:

```shell
pt Hy
```

This will return the following information:

- Name
- Symbol
- Atomic Number
- Atomic Mass
- Boiling Point
- Melting Point
- Discoverer
- Named by

If you want more properties, feel free to create an enhancement request.

Also note that the query is not case-sensitive (anymore).

## Possible future improvements

- [x] Element lookup is too slow. Find a way to speed it up.
  - Solution: Use a different library to store the elements.
  - Better solution: Use a json file to store the elements.
- [x] Add more information about the element.
  - Done: Added Boiling Point, Melting Point, Discoverer, and Named by.
- [x] Add search completion
  - Done
- [ ] Make improvements based on user feedback if there is any.

## Thanks to

- Bowserinator for maintaining the repository of the periodictable JSON file. You can find
  it [here](https://github.com/Bowserinator/Periodic-Table-JSON/blob/master/PeriodicTableJSON.json).
- flaticon, where the plugin icon comes from.[flaticon](https://www.flaticon.com/free-icons/periodic-table)

P.S. This is my first real contribution to an open source project. I hope you like it. If you have any suggestions or
improvements, please let me know.


