# pp_cmd_shift
Postprocessing command "shift"
Shift index by desired number of periods.
Usage example:
`... | shift a as b period=2, fill_value=0`

When period is not passed, shift index by 1.
fill_value: The scalar value to use for newly introduced missing values.


## Getting started
###  Prerequisites
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing
1. Create virtual environment with post-processing sdk 
```bash
make dev
```
That command  
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates `pp_cmd` directory with links to available post-processing commands
- creates `otl_v1_config.ini` with otl platform address configuration

2. Configure connection to platform in `otl_v1_config.ini`

### Test shift
Use `pp` to test shift command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  shift _time as new_time period=2, fill_value=0 
```
