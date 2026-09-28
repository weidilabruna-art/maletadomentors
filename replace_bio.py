with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the bio text
old = 'Já mentorei mais de 200 empreendedores que juntos faturaram múltiplos 7 dígitos.'

new_text = (
    '<p><span style="font-weight: 400;">Cristão, casado com a Weidila e estrategista digital com anos de experiência em marketing, tráfego e funis de vendas.</span></p>'
    '<p><span style="font-weight: 400;">Ajuda profissionais, especialistas e empresários a transformarem seu conhecimento em um negócio sólido no digital, com uma estrutura e metodologia que já geraram mais de <strong>R$10 milhões em vendas</strong>.</span></p>'
    '<p><span style="font-weight: 400;">Rubens já ajudou dezenas de profissionais a:</span></p>'
    '<p><span style="font-weight: 400;">– Transformarem conhecimento em um negócio<br>– Construírem um posicionamento forte e atraírem os clientes certos<br>– Terem mais previsibilidade, lucro e liberdade</span></p>'
)

if old in content:
    # Find the full paragraph block starting from old text
    start_marker = '<p><span style="font-weight: 400;">Já mentorei'
    end_marker = 'Algumas marcas com quem já trabalhei:</p>'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_text + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('OK - substituido com sucesso!')
    else:
        print(f'Markers not found: start={start_idx}, end={end_idx}')
else:
    print('ERRO - texto base nao encontrado')
    idx = content.find('mentorei')
    print(f'mentorei at: {idx}')
