{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    buildInputs = [
        (pkgs.haskellPackages.ghcWithPackages (pkgs: with pkgs; [ 
            data-default
            statistics
            mersenne-random-pure64
        ]))

		(pkgs.python3.withPackages (ps: with ps; [
		    pandas
		    matplotlib
            scipy
		  ]))
    ];
}
