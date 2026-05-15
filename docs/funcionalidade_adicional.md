# Funcionalidade Adicional

## Nome

Validação automática de reservas antes da confirmação.

## Descrição

Foi adicionada ao sistema uma etapa de validação executada antes da criação da reserva. Essa funcionalidade verifica se a solicitação atende às regras do sistema antes de confirmar o agendamento.

Na implementação atual, as regras adicionais são:

- impedir reservas em horários no passado;
- impedir que usuários que não sejam professores reservem laboratórios.
