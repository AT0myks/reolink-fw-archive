{
  description = "A reproducible Python development environment";

  inputs = {
    nixpkgs.url = "flake:nixpkgs";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Replace with your system architecture (e.g., "x86_64-darwin" for macOS)
      pkgs = import nixpkgs { inherit system; };

    in {
      devShells.${system} = {
        default = pkgs.mkShell {
          # List of packages available in the development shell
          packages = [
            pkgs.python3 # Installs a specific Python version (e.g., 3.11)
            pkgs.python3.pkgs.pip
            # Add other non-Python tools here, e.g., pkgs.jq
          ];

          # Environment variables or shell commands to run when entering the shell
          shellHook = ''
            export VENV_DIR=".venv"

            # Create and activate a virtual environment if it doesn't exist
            if [ ! -d "$VENV_DIR" ]; then
              echo "Creating virtual environment..."
              python3 -m venv "$VENV_DIR"
              source "$VENV_DIR"/bin/activate
              pip install aiohttp
            else
              source "$VENV_DIR"/bin/activate
            fi

            echo -e "\nVirtual environment activated."
            echo -e "\n> python download.py -h"
            
            python download.py -h
          '';
        };
      };
    };
}
