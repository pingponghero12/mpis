{ pkgs ? import <nixpkgs> {} }:

derivation {
  name = "hello";
  builder = "${pkgs.bash}/bin/bash";
  args = [ ./builder.sh ];
  inherit (pkgs) ghc;
  src = ./src;
  system = builtins.currentSystem;
}
