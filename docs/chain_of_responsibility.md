# Chain of Responsibility

## Autores

- Nicolas de Mello Freitas
- Lucas de Oliveira Kwok

## Objetivo no projeto

O padrão Chain of Responsibility foi aplicado para validar uma reserva em etapas, sem concentrar todas as regras em um único bloco de decisão. Assim, cada regra fica isolada em um validador e a reserva só continua no fluxo se a etapa atual for aprovada.

## Como está implementado

A classe abstrata ValidadorReserva representa o elo base da cadeia. Ela mantém a referência proximo e oferece o método definir_proximo, que encadeia os validadores.

Se algum validador retornar FALSE, a reserva é cancelada imediatamente. Se todos aprovarem, o fluxo segue para a política de conflito e depois para a criação da reserva.
