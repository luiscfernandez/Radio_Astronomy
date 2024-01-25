# Radio Astronomy Python scripts

Here I will be posting some python scripts that can automate sifting through radio data files for relevant information.  

### Time_Integration_Listr.py
This python script parses through the output listr file from AIPS and grabs all of the time integrated on source. It then calculates the total time integrated on source which can then be used to compare with total requested time on source to obtain actual theoretical noise rms.
 - Inputs: <pre>
   - Source: 'Name'                #Name of source (make sure file name contains source 'Name').
   - Param: 'seconds' or 'minutes' #Outputs total time as seconds or minutes, write in which is preferred.
   - Folder: './directory'         #Make sure folder directory where file(s) are located is correct.
</pre>
