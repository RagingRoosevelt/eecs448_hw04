#! /usr/bin/python

CurrentOrder = [];
Stock = [];
cost = 0;

titles = [0] * 61
authors = [0] * 61
genres = [0] * 61

def AddToOrder(BookID):
    CurrentOrder.append(titles[BookID])

def RemoveFromOrder(BookID):
    CurrentOrder.remove(titles[BookID])

def ListOrder():
    return CurrentOrder

def CalculateOrderCost():
    for i in CurrentOrder:
        for j in titles:
            if CurrentOrder[i] == titles[j]:
                if j < 21:
                    cost += 50
                if j < 41:
                    cost += 40
                else:
                    cost += 100

# Science Fiction Books, $50
titles[1] = 'Dune [S1]'
titles[2] = 'Ender\'s Game [S1]'
titles[3] = 'The Foundation Trilogy'
titles[4] = 'Hitch Hiker\'s Guide to the Galaxy [S1]'
titles[5] = '1984'
titles[6] = 'Stranger in a Strange Land'
titles[7] = 'Fahrenheit 451'
titles[8] = '2001: A Space Odyssey'
titles[9] = 'Do Androids Dream of Electric Sheep?'
titles[10] = 'Neuromancer [S1]'
titles[11] = '[C] I, Robot'
titles[12] = 'Starship Troopers'
titles[13] = 'Ringworld [S1]'
titles[14] = 'Rendezvous With Rama'
titles[15] = 'Hyperion [S1]'
titles[16] = 'Brave New World' 
titles[17] = 'The Forever War'
titles[18] = 'The Time Machine'
titles[19] = 'Childhood\'s End'
titles[20] = 'The Moon is a Harsh Mistress'

# Travel Books, $40
titles[21] = 'A Dragon Apparent'
titles[22] = 'A House in Bali'
titles[23] = 'A Moveable Feast'
titles[24] = 'A Short Walk in the Hindu Kush'
titles[25] = 'A Time of Gifts' 
titles[26] = 'A Turn in the South'
titles[27] = 'A Walk in the Woods'
titles[28] = 'A Winter in Arabia'
titles[29] = 'Among the Russians'
titles[30] = 'An Area of Darkness'
titles[31] = 'Arabian Sands'
titles[32] = 'Arctic Dreams'
titles[33] = 'The Art of Travel'
titles[34] = 'As I Walked Out One Midsummer Morning' 
titles[35] = 'Baghdad Without a Map'
titles[36] = 'Balkan Ghosts'
titles[37] = 'Beyond Euphrates'
titles[38] = 'The Bird Man and the Lap Dancer'
titles[39] = 'Bitter Lemons of Cyprus'
titles[40] = 'Black Lamb and Grey Falcon'

# Software Engineering Books, $100
titles[41] = 'Code Complete: A Handbook of Software Construction'
titles[42] = 'Head First Design Patterns'
titles[43] = 'Rapid Development' 
titles[44] = 'Design Patterns: Elements of Reusable Object-Oriented Software'
titles[45] = 'Cryptography: Protocols, Algorithms, and Source Code'
titles[46] = 'Agile Software Development: Principles, Patterns and Practices'
titles[47] = 'Joel on Software'
titles[48] = 'Peopleware: Productive Projects and Teams'
titles[49] = 'The Mythical Man-Month, Anniversary Edition'
titles[50] = 'Refactoring: Improving the Design of Existing Code'
titles[51] = 'Agile Estimating and Planning'
titles[52] = 'Writing Effective Use Cases' 
titles[53] = 'Object-Oriented Software Construction'
titles[54] = 'Software Estimation: Demystifying the Black Art'
titles[55] = 'User Stories Applied: For Agile Software Development'
titles[56] = 'The Art of Computer Programming'
titles[57] = 'Patterns of Enterprise Application Architecture' 
titles[58] = 'Mastering Regular Expressions'
titles[59] = 'The Pragmatic Programmer'
titles[60] = 'Software Requirements'

# Science Fiction Books, $50
authors[1] = 'Frank Herbert'
authors[2] = 'Orson Scott Card'
authors[3] = 'Isaac Asimov'
authors[4] = 'Douglas Adams'
authors[5] = 'George Orwell'
authors[6] = 'Robert A Heinlein'
authors[7] = 'Ray Bradbury'
authors[8] = 'Arthur C Clarke'
authors[9] = 'Philip K Dick'
authors[10] = 'William Gibson'
authors[11] = 'Isaac Asimov'
authors[12] = 'Robert A Heinlein'
authors[13] = 'Larry Niven'
authors[14] = 'Arthur C Clarke'
authors[15] = 'Dan Simmons'
authors[16] = 'Aldous Huxley'
authors[17] = 'Joe Haldeman'
authors[18] = 'H G Wells'
authors[19] = 'Arthur C Clarke'
authors[20] = 'Robert A Heinlein'

# Travel Books, $40
authors[21] = 'Norman Lewis'
authors[22] = 'Colin McPhee'
authors[23] = 'Ernest Hemingway'
authors[24] = 'Eric Newby'
authors[25] = 'Patrick Leigh Fermor'
authors[26] = 'V.S. Naipaul'
authors[27] = 'Bill Bryson'
authors[28] = 'Freya Stark'
authors[29] = 'Colin Thubron'
authors[30] = 'V.S. Naipaul'
authors[31] = 'Wilfred Thesiger'
authors[32] = 'Barry Lopez'
authors[33] = 'Alain de Botton'
authors[34] = 'Laurie Lee'
authors[35] = 'Tony Horwitz'
authors[36] = 'Robert D. Kaplan'
authors[37] = 'Freya Stark'
authors[38] = 'Eric Hansen'
authors[39] = 'Lawrence Durrell'
authors[40] = 'Rebecca West'

# Software Engineering Books, $100
authors[41] = 'Steve McConnell'
authors[42] = 'Elisabeth Freeman'
authors[43] = 'Steve McConnell'
authors[44] = 'Erich Gamma'
authors[45] = 'Bruce Schneier'
authors[46] = 'Robert C. Martin'
authors[47] = 'Joel Spolsky'
authors[48] = 'Tom DeMarco'
authors[49] = 'Frederick P. Brooks'
authors[50] = 'Martin Fowler'
authors[51] = 'Mike Cohn'
authors[52] = 'Alistair Cockburn'
authors[53] = 'Bertrand Meyer'
authors[54] = 'Steve McConnell'
authors[55] = 'Mike Cohn'
authors[56] = 'Donald E. Knuth'
authors[57] = 'Martin Fowler'
authors[58] = 'Jeffrey Friedl'
authors[59] = 'Andrew Hunt'
authors[60] = 'Karl E. Wiegers'

