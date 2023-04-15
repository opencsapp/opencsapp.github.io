import yaml

if __name__ == "__main__":
    with open('./programs_list.yml', 'r', encoding='utf-8') as f:
        content = yaml.safe_load(f)
    mkdocs_content = list()
    docs_content = list()
    for cata in content:
        (level, programs_dict), = cata.items()
        cs_programs = programs_dict['CS']
        noncs_programs = programs_dict['NONCS']
        if cs_programs is not None:
            cs_programs = sorted(cs_programs, key=lambda x: x.split('@')[-1] + x.split('@')[0])
        else:
            cs_programs = []
        if noncs_programs is not None:
            noncs_programs = sorted(noncs_programs, key=lambda x: x.split('@')[-1] + x.split('@')[0])
        else:
            noncs_programs = []
        programs = cs_programs + noncs_programs

        mkdocs_programs = programs.copy()
        for i, program in enumerate(mkdocs_programs):
            mkdocs_programs[i] = '{0}: {0}.md'.format(program)
        mkdocs_content.append({level: mkdocs_programs})

        docs_programs = programs.copy()
        for i, program in enumerate(docs_programs):
            docs_programs[i] = '[*{0}*]({0}.md)\n\n'.format(program) if program in noncs_programs else '[**{0}**]({0}.md)\n\n'.format(program)
        docs_content.append('### {0}\n\n'.format(level))
        docs_content += docs_programs

    mkdocs_content = yaml.dump(mkdocs_content, sort_keys=False, default_flow_style=False, allow_unicode=True).replace('\'', '')
    with open('mkdocs.yml', 'r', encoding="utf-8") as f:
        mkdocs_origin = f.read()
    with open('mkdocs.yml', 'w', encoding="utf-8") as f:
        f.write(mkdocs_origin.replace('$programs_list', mkdocs_content.replace('- ', '    - ')))
    with open('./docs/grade.md', 'r', encoding="utf-8") as f:
        docs_origin = f.read()
    with open('./docs/grade.md', 'w', encoding="utf-8") as f:
        f.write(docs_origin.replace('$programs_list', ''.join(docs_content)))

    with open('./blogs_list.yml', 'r', encoding='utf-8') as f:
        content = yaml.safe_load(f)
    docs_content = list()
    for blog in content:
        docs_content.append('[{0}]({0}.md)\n\n'.format(blog))
    with open('./docs/blog.md', 'r', encoding="utf-8") as f:
        docs_origin = f.read()
    with open('./docs/blog.md', 'w', encoding="utf-8") as f:
        f.write(docs_origin.replace('$blogs_list', ''.join(docs_content)))
