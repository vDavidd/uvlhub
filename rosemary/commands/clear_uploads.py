import click
import shutil
import os


@click.command('clear:uploads', help="Clears the 'uploads' directory.")
def clear_uploads():
    uploads_dir = '/app/uploads'

    # Verify if the 'uploads' folder exists
    if os.path.exists(uploads_dir) and os.path.isdir(uploads_dir):
        try:
            # Use shutil.rmtree to delete the folder and its contents.
            shutil.rmtree(uploads_dir)
            click.echo(click.style("The 'uploads' directory has been successfully cleared.", fg='green'))
        except Exception as e:
            click.echo(click.style(f"Error clearing the 'uploads' directory: {e}", fg='red'))
    else:
        click.echo(click.style("The 'uploads' directory does not exist.", fg='yellow'))
