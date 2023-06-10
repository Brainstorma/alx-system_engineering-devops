# 0x19. Postmortem - Practice Exercise

This postmortem describes a fake issue and its resolution for the 0x17-web_stack_debugging project, created for practice purposes.

## Issue Summary
Between 00:00 and 00:37 (10-06-2023, 12:11 am - 12:48 am GMT-1), all servers began returning a 500 error on all requests due to a recent server configuration update. The issue was caused by a mistyped reference in the WordPress settings file. The website was inaccessible to all users during the update.

## Timeline

00:00 - A lead developer noticed the website was returning a 500 error.

00:02 - Developer opened Ticket 0x19 and the servers were reverted to the most recent working change until the error was resolved to minimize downtime.

00:06 - A response to the ticket was received from junior developer Scout Curry.

00:10 - The `ps auxf` command showed that processes were running. Testing began by attaching `strace` to process IDs.

00:25 - Attaching `strace` to the apache2 process and sending a simple GET request to the server led to a -1 ENOENT error in one of the PHP files referenced by `phpp`.

00:27 - Using grep in the file location, the `phpp` error was traced to the `wp-settings.php` file due to a mistyped reference.

00:30 - A manual fix for the typo was made in the `wp-setting.php` file. After restarting Apache, the server returned a 200 code and displayed the correct website.

00:35 - A Puppet script using `sed` was created to remove the typo on all remaining servers. The script was run using `puppet apply`.

00:37 - All servers were updated with the new change.

## Corrective/Preventative measures
To prevent similar issues in the future, it is recommended to implement unit testing or pre-testing of code before pushing it to production. Alternatively, commit small changes in a way that allows change history to be easily reviewed on GitHub. This can help identify issues and prevent widespread downtime.
