# Parmana blog: instructions for Claude

Read [WRITING-GUIDE.md](WRITING-GUIDE.md) before you write, edit or review any post or page in this repository. It is the full guide. The rules below apply every time, even if the guide is not reopened.

## Standing rules

- **No em dashes or en dashes** in any text: posts, pages, templates, layouts and the guide itself.
- **Every post belongs to a series.** Set `series` and `series_part` in the front matter. Each new post takes the next part number, and it must be the next logical step after the last one.
- **Engineering posts** go in the series "Working on Parmana". That series is in logical, chronological order and focuses on how to maintain, understand and work on the code. Each part builds on the one before it and shows the commands and files involved.
- **Every title starts with its part number**, as `Part N: `, matching `series_part`.
- **Each post after part 1 refers back** to the part before it in its opening paragraph.
- **Every claim links to evidence**: a file, a test, or a document in the repository. If there is no evidence, say the claim is not yet verified, or leave it out.
- **Every post has a "What it does not do" section.**
- **Start new posts from [templates/post-template.md](templates/post-template.md).** Date and time go in the front matter as `YYYY-MM-DD HH:MM:SS +0000`.
- **No secrets, keys, customer data, or unresolved security findings** in any post.
- **Do not push directly to `main`.** Work on a branch and open a pull request.
