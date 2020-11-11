

exports.loginPatient = (req, res, next) => {
  User.findOne({ numesecu: req.body.numesecu })
    .then(user => {
      if (!user) {
        return res.status(401).json({ error: 'Numéro de sécurité sociale non identifié !' }); //le numero de sécu n'est pas reconnu
      }
    })
    .catch(error => res.status(500).json({ error })); // autre erreur
};


exports.loginMedecin = (req, res, next) => {
  User.findOne({ rpps: req.body.rpps })
    .then(user => {
      if (!user) {
        return res.status(401).json({ error: 'RPPS non reconnu !' }); // le rpps n'est pas reconnu 
      }
    })
    .catch(error => res.status(500).json({ error })); //autre erreur
};
