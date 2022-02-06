import debugpy
import pytest


def main() -> None:
    print("Attach vscode to debugger on port 62888")
    debugpy.listen(62888)
    debugpy.wait_for_client()  # blocks execution until client is attached
    pytest.main()


if __name__ == "__main__":
    main()
