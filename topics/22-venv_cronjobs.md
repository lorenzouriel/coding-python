# Running Python Scripts with Cronjobs

To schedule your Python scripts to run every night at 6pm using cron on Linux, follow the steps below:

**1. Open terminal**

**2. Edit the crontab using the command:**
```bash
crontab -e
```
- When you run `crontab -e`, you are being asked to choose an editor to edit the crontab file. If you want the easiest option, type `1` and press Enter to use `Nano`.

**3. Add your script to crontab:**
```bash
0 18 * * * /home/local/data-flow-batch/.venv/bin/python /home/local/data-flow-batch/seu_script.py
```

- Note: Replace /home/local/data-flow-batch/seu_script.py with the actual path of your Python script.

**4. Save and exit the editor:**
On Nano, you can save by pressing `CTRL + O`, then Enter, and exit by pressing `CTRL + X`.

**5. Check crontab:**
To ensure your cron job was added correctly, you can use the command:
```bash
crontab -l
```

**6. Check log:**
To check your cron log execution, you can run:
```bash
sudo grep -i cron /var/log/syslog
```

### Breakdown of Each Line
Each line has the following structure:
```bash
* * * * * command
```

Where the five asterisks represent time and date fields, and the command is what you want to run.

**1. Time and Date Fields: The five fields are as follows**
- Minute (0-59): The minute of the hour when the command should run.
- Hour (0-23): The hour of the day when the command should run (0 is midnight, 1 is 1 AM, etc.).
- Day of the Month (1-31): The day of the month when the command should run
- Month (1-12): The month of the year when the command should run.
- Day of the Week (0-7): The day of the week when the command should run (0 and 7 represent Sunday).

#### Your Specific Lines Explained
Given your specific lines:
```bash
0 18 * * * /home/local/data-flow-batch/.venv/bin/python /home/local/data-flow-batch/seu_script.py
0 18 * * * /home/local/data-flow-batch/.venv/bin/python /home/local/data-flow-batch/seu_script.py
0 18 * * * /home/local/data-flow-batch/.venv/bin/python /home/local/data-flow-batch/seu_script.py
```

- `0 18 * * *`: This indicates that the command should run at 18:00 (6 PM) every day. The breakdown is:
    - `0`: At the 0th minute (exactly at the top of the hour).
    - `18`: At the 18th hour (6 PM).
    - `*`: Every day of the month.
    - `*`: Every month.
    - `*`: Every day of the week.

- The command to run is:
    - `/home/local/data-flow-batch/.venv/bin/python`: This is the path to the Python interpreter within a virtual environment (`.venv`). It ensures that the correct Python version and libraries are used.
    - `/home/local/data-flow-batch/seu_script.py`: This is the path to the specific Python script you want to run (where `scriptX.py` can be `script1.py`, `script2.py`, or `script3.py`).

### Summary
In summary, each of these lines schedules a Python script to be executed every day at 6 PM. The scripts are executed using a specific Python interpreter located in a virtual environment, ensuring that any dependencies required by the scripts are available. If you want to ensure that the scripts are running properly, you can check their output, log files, or any other method of validation to confirm successful execution.