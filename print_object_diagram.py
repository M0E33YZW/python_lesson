LinkedList = [None, None]

def print_object_diagram(list):
   
    print('```plantuml')
    print('@startuml\n')
    print('map ' + str(id(list.head)) +' {')
    print('    class => Node')
    print('    value => ' + str(list.head))
    print('    next => ' + str(list.next))
    print('}\n')
    
    print('map ' + str(id(list)) +' {')
    print('    class => List')
    print('    head *-> ' + str(list.head))
    print('}\n')

    print('@enduml')
    print('```\n')

print('# Object diagram \n')

list = LinkedList
print('## LinkedList()\n')
print_object_diagram(list)


def print_object_diagram(list):
   
    print('```plantuml')
    print('@startuml\n')
    print('map ' + str(id(list[1])) +' {')
    print('    class => Node')
    print('    value => ' + str(id(list[1])))
    print('    next *-> ' + str(id(list[2])))
    print('}\n')

    print('map ' + str(id(list[1])) +' {')
    print('    class => Node')
    print('    value => ' + str(id(list[0])))
    print('    next *-> ' + str(id(list[1])))
    print('}\n')
    
    print('map ' + str(id(list[0])) +' {')
    print('    class => List')
    print('    head *-> ' + str(id(list[1])))
    print('}\n')

    print('@enduml')
    print('```\n')

list.append(3)
print('## insert(3)')

print_object_diagram(list)