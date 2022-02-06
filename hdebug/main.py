import debugpy
import pytest
import os

def main() -> None:
    print("Attach vscode to debugger on port 62888")
    os.environ["PYDEVD_DEBUG"] = "1"
    debugpy.log_to('logs/')
    debugpy.listen(62888)
    debugpy.wait_for_client()
    pytest.main()


if __name__ == "__main__":
    main()
