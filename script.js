const kcalPorHora = {
  corrida: 600, caminhada: 300, inclinada: 450, bicicleta: 400, escada: 550
};
const nomesExercicio = {
  corrida: 'Esteira correndo', caminhada: 'Esteira caminhando',
  inclinada: 'Esteira inclinada', bicicleta: 'Bicicleta ergométrica', escada: 'Escada'
};

function calcular() {
  const ex  = document.getElementById('exercicio').value;
  const cal = parseFloat(document.getElementById('calorias').value);
  const min = parseFloat(document.getElementById('minutos').value);
  const ses = parseInt(document.getElementById('sessoes').value);

  if (!ex || !cal || !min) {
    alert('Preencha todos os campos para calcular.');
    return;
  }

  const kcalH      = kcalPorHora[ex];
  const kcalSessao = Math.round(kcalH * (min / 60));
  const kcalSemana = kcalSessao * ses;
  const semanas    = Math.ceil(cal / kcalSemana);
  const meses      = (semanas / 4.33).toFixed(1);

  document.getElementById('res-semanas').textContent = semanas;
  document.getElementById('res-kcal').textContent    = kcalH;
  document.getElementById('res-sessao').textContent  = kcalSessao;
  document.getElementById('res-semana').textContent  = kcalSemana;

  let emoji = semanas <= 8 ? '🚀' : semanas <= 16 ? '💪' : '🎯';
  document.getElementById('res-desc').innerHTML =
    `${emoji} Com <strong>${nomesExercicio[ex]}</strong>, fazendo <strong>${min} minutos</strong> por sessão e <strong>${ses}× por semana</strong>, você vai queimar <strong>${kcalSemana} kcal/semana</strong> e atingir a meta de <strong>${cal.toLocaleString('pt-BR')} kcal</strong> em aproximadamente <strong>${semanas} semanas</strong> (~${meses} meses). Continue firme!`;

  const res = document.getElementById('resultado');
  res.classList.remove('show');
  void res.offsetWidth;
  res.classList.add('show');
}

function alternarMenu() {
  const m = document.getElementById('menuMobile');
  m.classList.toggle('open');
}

document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});
