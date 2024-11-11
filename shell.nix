
{ sources ? import ./npins }:
let
  pkgs = import sources.nixpkgs { config = {}; overlays = []; };
  pythonPackages = pkgs.python3Packages;
in pkgs.mkShell rec {
  buildInputs = with pkgs; [
    pythonPackages.numpy
    pythonPackages.matplotlib
    pythonPackages.ipykernel
    pythonPackages.pandas
    pythonPackages.seaborn

    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pythonPackages.python
  ];

}
