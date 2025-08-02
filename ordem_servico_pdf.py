#!/usr/bin/env python3
"""
Sistema de Geração de PDF para Ordens de Serviço
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime

def gerar_pdf_ordem_servico(dados_ordem, caminho_saida):
    """
    Gera PDF da ordem de serviço em formato A4
    """
    doc = SimpleDocTemplate(caminho_saida, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Estilo personalizado para título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    # Cabeçalho
    story.append(Paragraph("ORDEM DE SERVIÇO", title_style))
    story.append(Spacer(1, 20))
    
    # Informações da empresa
    empresa_data = [
        ['SISTEMA JAM', ''],
        ['Endereço: Rua das Inovações, 123', ''],
        ['Telefone: (11) 99999-9999', ''],
        ['Email: contato@sistemajam.com.br', '']
    ]
    
    empresa_table = Table(empresa_data, colWidths=[4*inch, 2*inch])
    empresa_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(empresa_table)
    story.append(Spacer(1, 20))
    
    # Dados da ordem
    ordem_data = [
        ['Número da OS:', dados_ordem.get('id', 'OS-001')],
        ['Data:', dados_ordem.get('data', datetime.now().strftime('%d/%m/%Y'))],
        ['Status:', dados_ordem.get('status', 'Em Andamento')]
    ]
    
    ordem_table = Table(ordem_data, colWidths=[2*inch, 4*inch])
    ordem_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(ordem_table)
    story.append(Spacer(1, 20))
    
    # Dados do cliente
    story.append(Paragraph("DADOS DO CLIENTE", styles['Heading2']))
    cliente_data = [
        ['Nome:', dados_ordem.get('cliente', 'Cliente')],
        ['Telefone:', dados_ordem.get('telefone', '(11) 99999-9999')],
        ['Email:', dados_ordem.get('email', 'cliente@email.com')]
    ]
    
    cliente_table = Table(cliente_data, colWidths=[2*inch, 4*inch])
    cliente_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(cliente_table)
    story.append(Spacer(1, 20))
    
    # Detalhes do serviço
    story.append(Paragraph("DETALHES DO SERVIÇO", styles['Heading2']))
    servico_data = [
        ['Tipo de Serviço:', dados_ordem.get('servico', 'Serviço')],
        ['Descrição:', dados_ordem.get('descricao', 'Descrição do serviço')],
        ['Valor:', dados_ordem.get('valor', 'R$ 0,00')]
    ]
    
    servico_table = Table(servico_data, colWidths=[2*inch, 4*inch])
    servico_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightyellow),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(servico_table)
    story.append(Spacer(1, 20))
    
    # Observações
    if dados_ordem.get('observacoes'):
        story.append(Paragraph("OBSERVAÇÕES", styles['Heading2']))
        story.append(Paragraph(dados_ordem['observacoes'], styles['Normal']))
        story.append(Spacer(1, 20))
    
    # Assinaturas
    story.append(Paragraph("ASSINATURAS", styles['Heading2']))
    assinaturas_data = [
        ['Cliente:', ''],
        ['', ''],
        ['', ''],
        ['Técnico:', ''],
        ['', ''],
        ['', '']
    ]
    
    assinaturas_table = Table(assinaturas_data, colWidths=[3*inch, 3*inch])
    assinaturas_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, 1), (0, 2), 1, colors.black),
        ('LINEBELOW', (1, 1), (1, 2), 1, colors.black),
        ('LINEBELOW', (0, 4), (0, 5), 1, colors.black),
        ('LINEBELOW', (1, 4), (1, 5), 1, colors.black)
    ]))
    story.append(assinaturas_table)
    
    # Gerar PDF
    doc.build(story)
    return caminho_saida

def enviar_whatsapp(numero, mensagem):
    """
    Função para enviar WhatsApp (simulada)
    """
    # Em produção, você usaria a API do WhatsApp Business
    print(f"Enviando WhatsApp para {numero}: {mensagem}")
    return True

if __name__ == "__main__":
    # Exemplo de uso
    dados_exemplo = {
        'id': 'OS-001',
        'data': '02/08/2024',
        'status': 'Em Andamento',
        'cliente': 'João Silva',
        'telefone': '(11) 99999-9999',
        'email': 'joao@email.com',
        'servico': 'Manutenção de Computador',
        'descricao': 'Manutenção preventiva e limpeza do sistema',
        'valor': 'R$ 150,00',
        'observacoes': 'Sistema funcionando normalmente após manutenção'
    }
    
    pdf_path = gerar_pdf_ordem_servico(dados_exemplo, 'ordem_servico.pdf')
    print(f"PDF gerado: {pdf_path}") 