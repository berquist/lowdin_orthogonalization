#include <armadillo>

int main() {

    arma::mat S;
    S.load("S.dat", arma::arma_ascii);
    S.print("Overlap matrix");

    arma::vec lam_s_vec;
    arma::mat l_s;
    arma::eig_sym(lam_s_vec, l_s, S);
    arma::mat lam_s_mat = arma::diagmat(lam_s_vec);
    arma::mat lam_sqrt_inv = arma::sqrt(arma::inv(lam_s_mat));
    arma::mat symm_orthog = l_s * lam_sqrt_inv * l_s.t();

    symm_orthog.print("Symmetric orthogonalization matrix");

    return 0;
}
