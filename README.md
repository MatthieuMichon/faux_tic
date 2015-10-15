# faux_tic
Tele information client

## Datagrams


|Name|Label|Size (chars)|Unit|
|---|---|---|---|
|Meter address|ADCO|12|None|
|Plan|OPTARIF|4|None|
|Current cap|ISOUSC|2|A|
|Index (*Base* plan)|BASE|9|Wh|
|Real-time current|IINST|3|A|
|Rated power exceeded warning|ADPS|3|A|
|Maximum current used|IMAX|3|A|
|Complex power|PAPP|5|VA|
|Meter status|MOTDETAT|6|None|

### Details

* **Meter address**: meter identification address, coded on 12 numerical ASCII chars
* **Plan**: selected plan, coded on four alphanumerical ASCII chars
* **Current cap**: highest sustainable electrical current, coded on two numerical ASCII chars
* **Index**: electrical energy consumption index, coded on nine numerical ASCII chars
* **Real-time current**: Active (in-phase) real-time current, coded on 3 numerical ASCII chars
* **Rated power exceeded warning**: *TBD*, coded on 3 numerical ASCII chars
* **Maximum current used**: Highest recorded real-time current, coded on 3 numerical ASCII chars
* **Complex power**: Complex power, coded in five numerical ASCII chars, rounded to the closest dozen
* **Meter status**: Meter internal status, 24-bit structure coded on six hexadecimal chars

### Format

Datagrams are encoded in a human readable markup.

JSON output with extra comments:
```javascript
// comments must not be present in the JSON object
{
  "ADCO": "123456789012", // example
  "OPTARIF": "BASE", // BASE or HC.. or EJP. or BBR[0-9A-Z]
  "ISOUSC": "30",
  "BASE": "000010023",
  "IINST": "011",
  "APDS": "000", // waiting hard data
  "IMAX": "029",
  "PAPP": "04350",
  "MOTDETAT": "41FF01" // example
}
```

YAML: maybe better suited for single-board MCUs ?
```yaml
{
  - ADCO: 123456789012 # example
  - OPTARIF: BASE # BASE or HC.. or EJP. or BBR[0-9A-Z]
  - ISOUSC: 30
  - BASE: 000010023
  - IINST: 011
  - APDS: 000 # waiting hard data
  - IMAX: 029
  - PAPP: 04350
  - MOTDETAT: 0x41FF01 # example
}
```

## Implementation

The implementation is intended to be a simple as practical. It relies on the following systems:

* A MCU board with network connectivity
* A computer executing two server instances:
** a software program receiving and processing data coming from the MCU
** a HTTP server delivering HTML pages containing the previous processed data

