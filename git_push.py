import subprocess

def git_push(branch_name):
    """Push the specified branch to the remote repository."""
    try:
        result = subprocess.run(['git', 'push', 'origin', branch_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error pushing branch {branch_name}: {e.stderr.decode()}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python git_push.py <branch_name>")
    else:
        branch_name = sys.argv[1]
        git_push(branch_name)
