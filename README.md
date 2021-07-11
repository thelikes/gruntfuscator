# gruntfuscator

Simple script to obfuscate Grunt strings

Adapted from: [Fixing Some .NET Tradecraft](https://operat-or.gitbook.io/notes/fixing-some-.net-tradecraft)

## Implementation
- Random replace for 'Grunt' , 'Covenant' , and 'Stage'
- Hard-coded replace for 2 GUID strings

## Usage

1. Install Cov
2. Head to Templates > GruntHTTP
3. Copy the Stager code into stager.cs
4. Copy the Executor code into executor.cs
5. Run the py scipt

```
python3 gruntfuscator.py stager.cs obf-stager.cs
python3 gruntfuscator.py executor.cs obf-executor.cs
```

6. Copy the contents of each back into the GUI's template

Finally, create your listener, then launcher(s).

## Tips

- the Stager and Executor can be compiled in Visual Studio and
  ThreatCheck/DefenderCheck can be run on them
- Change the hard-coded replaces
- Add more strings to be replaced
- Throw in an AMSI bypass
