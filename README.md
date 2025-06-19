# StoryAgents

A multi-agent, role-playing story generation system powered by LLMs. Agents with distinct personalities interact in a fantasy world, collaboratively advancing a story and producing a polished narrative summary.

## Features

- **Multi-agent interaction**: Agents (e.g., royal advisor, forest shaman, mountain chieftain) each have unique personas and abilities.
- **World rules**: The story unfolds in a fantasy world with its own logic and lore.
- **Dynamic controller**: A controller agent decides which character acts next, encouraging rich, multi-party dialogue.
- **Automated summarization**: After a set number of turns, a summarizer agent produces a coherent, emotionally rich story.
- **Logging**: All actions and agent turns are logged for transparency and debugging.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/LC-John/StoryAgents.git
cd StoryAgents
```

### 2. Install dependencies

We recommend using uv.

```bash
uv sync
```

### 3. Set up environment variables

Create a `.env` file in the project root with your DeepSeek API key:

```bash
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 4. Run the project

```bash
python main.py
```

The story will be generated in the console, and logs will be saved to `story_agents.log`.

## A Demonstrative Story

### Role-playing Script

#### ===== Init World State =====

The world is in a state of peace, but tensions are rising as the mysterious magic item found at the border of the Kingdom, the Forest, and the Tribe has sparked curiosity and competition among the factions. Rumors suggest the item holds immense power, and each faction is considering how to claim or neutralize it to maintain the balance of power.

#### ===== Forest Shaman's Round =====

```
<think> The winds whisper of unrest... The magic item found at the borders stirs the hearts of many. The Forest feels uneasy, the trees murmur warnings. I must tread carefully, for balance is fragile.</think>

<action> Thorn steps forward from the shadows of the ancient oaks, his twisted staff glowing faintly with green energy. His braided hair sways slightly as he tilts his head, listening to the rustling leaves.</action>

<speak> The Forest speaks of a disturbance... a power that does not belong to any one faction. It is not for the Kingdom, nor the Tribe, nor even the Forest to claim. Such things must be handled with care, lest we upset the balance.</speak>

<think> Grimrock's presence is strong, like the mountains themselves. Eldara's wisdom is deep, but even she may not see the full picture. I must ensure they understand the danger.</think> 

<action> Thorn raises his staff slightly, the green light pulsing as if in rhythm with his heartbeat. His eyes flicker with the same energy as he looks between Grimrock and Eldara.</action>

<speak> We stand at a crossroads, friends. The earth trembles, the rivers murmur, and the winds carry warnings. This magic item... it is not a prize to be won, but a test of our unity. Will we let greed divide us, or will we work together to preserve the balance?</speak>
```

#### ===== Round 1 World State =====

The world remains in a fragile peace, but Thorn's warning about the magic item has heightened tensions. The Forest's unease is palpable, and the other factions are now more aware of the potential dangers. The Kingdom, the Tribe, and the Forest are each weighing their next moves, with Thorn advocating for unity and caution. The magic item's presence continues to stir curiosity and fear, and the balance of power hangs in the balance.

#### ===== Mountain Chieftain's Round =====

```
<action> Grimrock strokes his thick beard thoughtfully, the spikes on his helmet glinting in the dim light. His dark eyes narrow as he listens to Thorn's words, the fire within him flickering like the forge's flame.</action>

<think> Hmph. The shaman speaks of balance, but what does a tree-hugger know of dwarven steel and mountain gold? Still... if there's a magic item stirring trouble, best not let the elves get their delicate hands on it first. </think>

<speak> Aye, Thorn, the earth does tremble—but not from fear. It shakes with the weight of dwarven boots marchin’ to meet whatever threat this magic bauble poses! </speak>

<action> He unslings his battle-axe and rests it against his shoulder, the weight familiar and comforting. The wine pot at his waist sways as he takes a step forward, his shield clanking against his armor.</action>

<speak> If this thing’s dangerous, then let the Tribe forge a cage for it—stronger than elven spells and deeper than any forest root. But mark my words, shaman—if it’s treasure, then by stone and sweat, it’ll be ours to claim fair and square! </speak>

<think> And if Eldara thinks her pretty words will sway me, she’s got another thing coming. The last time elves "advised" us, we ended up with a treaty that favored their silver tongues over our honest labor. </think>

<action> He takes a swig from his wine pot, wiping his mouth with the back of his hand before glaring between Thorn and Eldara.</action>

<speak> So, what’s it to be? Do we stand here jawin’ like nervous goats, or do we act like warriors and face this thing head-on? </speak>
```

#### ===== Round 2 World State =====

The world remains in a fragile peace, but tensions have escalated as Grimrock's declaration of dwarven dominance over the magic item clashes with Thorn's plea for unity. The Forest's unease grows, and the Kingdom's cautious stance is now challenged by the Tribe's boldness. The magic item's presence has become a focal point of factional rivalry, threatening the delicate balance. Thorn's warnings are met with skepticism, and Eldara's wisdom is needed to mediate before the situation spirals into conflict.

#### ===== Royal Advisor's Round =====

```
<action> Eldara stands with her crystal-topped staff held firmly in both hands, her azure robes flowing gently as if stirred by an unseen breeze. Her melancholic blue eyes shift between Thorn and Grimrock, weighing their words with the patience of centuries.</action>

<think> Thorn speaks of balance, yet his words carry the weight of the Forest's unease. Grimrock's boldness is expected, but his eagerness could ignite a conflict none of us can afford. The magic item... it must not become a symbol of division. The Kingdom's stability hinges on wisdom, not force.</think>

<speak> "Thorn, your counsel is heard, and the Forest's whispers are not ignored. Grimrock, your strength is undeniable, but even the mightiest axe cannot cleave through fate's weave."</speak>

<action> She raises her staff slightly, the crystal at its tip glowing with a soft, steady light. Her voice remains calm, but there is an undercurrent of authority—the tone of one who has guided kings and shaped laws.</action>

<speak> "This artifact is no mere trinket to be claimed or caged. It is a thread in the tapestry of our world, and its placement must be deliberate. The Kingdom proposes a council—a gathering of minds from each faction to study its nature and determine its rightful path. Let us not act in haste, lest we unravel what centuries of peace have woven."</speak>

<think> The king would approve of this approach. It maintains the Kingdom's role as mediator while acknowledging the concerns of the others. But will Thorn's idealism and Grimrock's pride allow for compromise?</think>

<action> She turns her gaze fully to Grimrock, her expression unreadable but her eyes piercing. "Would the Tribe honor such a gathering, or must we test our wills against one another first?"</action>
```

#### ===== Round 3 World State =====

The world remains in a fragile peace, but tensions have escalated further as Grimrock's declaration of dwarven dominance clashes with both Thorn's plea for unity and Eldara's proposal for a council. The Forest's unease grows, and the Kingdom's cautious stance is now challenged by the Tribe's boldness. The magic item's presence has become a focal point of factional rivalry, with Thorn advocating for balance, Grimrock asserting dwarven claim, and Eldara proposing a diplomatic solution. The situation teeters on the edge of conflict, with each faction's next move critical to maintaining or shattering the peace.

#### ===== Forest Shaman's Round =====

```
<think> Grimrock's fire burns bright, but it blinds him to the deeper currents. Eldara's wisdom is vast, yet even she may not fully grasp the Forest's unease. The magic item... it hums with a power that does not belong to any one hand. The balance trembles.</think>

<action> Thorn closes his eyes for a moment, listening to the rustling leaves and the distant call of a hawk. The green light in his staff pulses softly, mirroring the rhythm of his breath. When he opens his eyes again, the sparks within them glow brighter.</action>

<speak> "Grimrock, your strength is like the mountain's roots—unyielding. But even the deepest stone cracks under the weight of imbalance. Eldara, your council is wise, but councils take time, and the Forest's whispers grow urgent."</speak>

<action> He plants his staff firmly into the earth, and the ground beneath them shivers slightly, as if in agreement. The charms woven into his braids clink softly, stirred by an unseen wind.</action>

<speak> "This artifact is not a thing to be claimed, nor a riddle to be solved by debate alone. It is a living thread, woven into the world's fabric. If we pull too hard, the weave may fray. I propose a different path—let it choose its own keeper. Let the magic decide, as it always has."</speak>

<think> The dwarves will bristle at this, and the elves may hesitate. But the Forest does not lie—the item's will is its own. If they cannot see that, the consequences will be dire.</think>

<action> Thorn's gaze lingers on the horizon, where the trees sway uneasily. His voice drops, carrying the weight of prophecy. "The winds carry a warning. Heed it, or we will all answer to the storm."</action>
```

#### ===== Round 4 World State =====

The world teeters on the brink of conflict as Thorn's proposal for the magic item to choose its own keeper clashes with Grimrock's assertion of dwarven claim and Eldara's call for a diplomatic council. The Forest's unease intensifies, its whispers growing more urgent, while the Tribe's boldness and the Kingdom's cautious diplomacy strain the fragile peace. The magic item's presence has become a focal point of tension, with each faction's stance hardening. The next move could either defuse the situation or ignite a full-scale confrontation.

#### ===== Mountain Chieftain's Round =====

```
<action> Grimrock lets out a deep, rumbling chuckle, his thick beard bristling as he shakes his head. He tightens his grip on his battle-axe, the metal creaking under his calloused fingers.</action>

<think> *Aye, the shaman speaks of magic choosing its keeper, and the elf wants a council. Both sound like fancy ways of saying "let’s waste time while someone else takes what’s ours."* </think>

<speak> "Thorn, yer Forest whispers may be urgent, but the mountains don’t whisper—they roar. And right now, they’re tellin’ me that sittin’ around waitin’ for some trinket to pick a favorite is a fool’s game!" </speak>

<action> He slams the butt of his axe into the ground, sending a small tremor through the earth. The wine pot at his waist sloshes as he leans forward, his dark eyes burning like coals.</action>

<speak> "Eldara, yer council sounds like a fine way for the Kingdom to talk us in circles while they sneak off with the prize. And Thorn—yer ‘let it choose’ idea? Sounds like a quick path to chaos. If this thing’s got a mind of its own, then it’ll respect strength, and there’s none stronger than dwarven steel!" </speak>

<think> *If the elves and the tree-folk won’t act, then the Tribe will. Better to seize it now than regret it later.* </think>

<action> He takes another swig from his wine pot, then wipes his mouth with the back of his hand, glaring at both of them.</action>

<speak> "So here’s my counter-proposal: we go to the damned thing together—no sneakin’, no schemin’—and let it see who’s worthy. If it truly chooses, then fine. But if it’s just sittin’ there waitin’ to be claimed, then by my beard, the first hand on it gets to keep it!" </speak>

<action> He hefts his axe onto his shoulder, the spikes on his helmet catching the light as he grins fiercely.</action>

<speak> "What say ye? Or are ye both too busy talkin’ to act?" </speak>
```

#### ===== Round 5 World State =====

The world teeters on the brink of conflict as Thorn's proposal for the magic item to choose its own keeper clashes with Grimrock's assertion of dwarven claim and Eldara's call for a diplomatic council. The Forest's unease intensifies, its whispers growing more urgent, while the Tribe's boldness and the Kingdom's cautious diplomacy strain the fragile peace. The magic item's presence has become a focal point of tension, with each faction's stance hardening. Grimrock's challenge to confront the artifact directly adds fuel to the fire, risking an open clash if the others refuse. The next move could either defuse the situation or ignite a full-scale confrontation.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's grip tightens slightly on her staff, the crystal at its tip flickering with a subdued azure glow. Her silver hair cascades over her shoulders as she tilts her head, her melancholic eyes reflecting the weight of centuries of diplomacy and conflict.</action>

<think> Grimrock's brashness is as predictable as the tides, but his proposal carries a dangerous simplicity. Thorn's idealism is noble, yet naive—magic items may choose, but factions will still war over the chosen. The king would counsel patience, but patience wears thin when axes are raised.</think>

<speak> "Grimrock, your courage is as unyielding as the mountains you hail from, but even the mightiest peak knows when to stand firm and when to yield. Thorn, your faith in the artifact's will is... poetic, but the world is not governed by poetry alone."</speak>

<action> She steps forward, her robes whispering against the earth, and levels her gaze at Grimrock, then Thorn, her voice measured but firm.</action>

<speak> "Very well. If you insist on confronting the artifact directly, then let it be done—but not as a free-for-all. We three shall approach it together, as representatives of our factions. No blades drawn, no spells cast. Let it sense our intentions, not our violence. And when it chooses—if it chooses—we abide by its decision. That is the Kingdom's condition."</speak>   

<think> A gamble, but one that may yet preserve the peace. If the artifact rejects us all, it will force humility upon them. If it chooses one... then the others must honor their word—or face the consequences.</think>

<action> She turns slightly, her staff's light casting a faint glow over the tense space between them. Her voice softens, but only slightly.</action>

<speak> "Or do you fear the judgment of magic itself, Grimrock? Thorn?"</speak>
```

#### ===== Round 6 World State =====

The world teeters on the brink of conflict as Thorn's proposal for the magic item to choose its own keeper clashes with Grimrock's assertion of dwarven claim and Eldara's call for a diplomatic council. The Forest's unease intensifies, its whispers growing more urgent, while the Tribe's boldness and the Kingdom's cautious diplomacy strain the fragile peace. The magic item's presence has become a focal point of tension, with each faction's stance hardening. Grimrock's challenge to confront the artifact directly adds fuel to the fire, risking an open clash if the others refuse. The next move could either defuse the situation or ignite a full-scale confrontation. Eldara's proposal for a joint approach to the artifact has been put forward, but Thorn's concerns about the Forest's warnings and Grimrock's impatience remain unresolved. The artifact's choice—or lack thereof—will determine the fate of the fragile alliance between the factions.

#### ===== Forest Shaman's Round =====

```
<think> Grimrock's stubbornness is like a boulder in a river—unmoving, yet causing ripples that disturb all around it. Eldara seeks order, but even her wisdom may not see the storm brewing beneath the surface. The Forest's whispers grow louder, more insistent. The artifact is not just a test of unity—it is a harbinger.</think>

<action> Thorn exhales slowly, the green light in his staff dimming momentarily as if mirroring his contemplation. He lifts his gaze to meet Eldara's, then Grimrock's, his eyes flickering like distant lightning in a storm.</action>

<speak> "Eldara, your condition is fair. Grimrock, your courage is undeniable. But hear this—the artifact does not merely 'choose.' It *answers.* It answers the call of the world's balance, and if we approach it with divided hearts, it will answer in kind."</speak>

<action> He presses his palm against the bark of the nearest tree, closing his eyes as if listening. The leaves above rustle urgently, and a single feather woven into his braid trembles.</action>

<speak> "Very well. We three shall approach it together. But know this: if the artifact's answer is one we do not expect—if it speaks in ways we do not understand—we must heed it. Not as Kingdom, Tribe, or Forest, but as guardians of this world."</speak>

<think> The winds shift. The Forest holds its breath. Whatever comes next... it will change everything.</think>

<action> Thorn pulls his staff from the earth, the green light flaring once more as he turns toward the distant glade where the artifact rests. His voice is low, carrying the weight of prophecy.</action>

<speak> "Lead the way, then. But tread lightly. The earth remembers every step."</speak>
```

#### ===== Round 7 World State =====

The world teeters on the brink of a decisive moment as Thorn, Grimrock, and Eldara agree to approach the artifact together, each bound by their own convictions. The Forest's whispers grow urgent, the mountains rumble with impatience, and the Kingdom's diplomatic veneer strains under the weight of impending choice. The artifact's decision—or lack thereof—will either solidify the fragile alliance or shatter it entirely. The factions' representatives now stand united in purpose but divided in intent, their next actions poised to reshape the balance of power. The magic item's true nature remains unknown, but its influence over the world's fate is undeniable.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's fingers trace the intricate silver embroidery of her robe, her gaze lingering on the distant glade where the artifact rests. The crystal atop her staff pulses faintly, mirroring the rhythm of her measured breaths.</action>

<think> Thorn speaks of balance, yet his trust in the artifact's will borders on recklessness. Grimrock's bravado is a spark waiting to ignite a wildfire. The Kingdom's stability hinges on this moment—I cannot afford missteps. If the artifact chooses, it must choose wisely. If it rejects us all... perhaps that is the best outcome.</think>

<speak> "Then let us proceed, but with caution. The artifact's power is unknown, and its judgment may not align with our expectations."</speak>

<action> She lifts her staff slightly, the crystal's glow brightening to illuminate the path ahead. Her voice carries the weight of centuries, calm but unyielding.</action>

<speak> "Remember, we approach as representatives, not conquerors. Let no blade be drawn, no spell cast in haste. The artifact will sense our intentions—let them be pure."</speak>

<think> The king would approve of this measured approach. But if Grimrock's axe or Thorn's magic disrupts the balance... I must be ready to intervene. The holy laws demand it.</think>     

<action> She steps forward, her azure robes flowing like water over the earth, and glances back at Thorn and Grimrock, her blue eyes piercing.</action>

<speak> "Follow, if you will. But heed the silence between your steps—it often speaks louder than words."</speak>
```

#### ===== Round 8 World State =====

The representatives of the Forest, the Tribe, and the Kingdom have agreed to approach the mysterious artifact together, each bound by their own convictions but united in purpose. Thorn's connection to nature warns of impending imbalance, Grimrock's dwarven pride demands action, and Eldara's diplomatic wisdom seeks to mediate. The artifact's true nature remains unknown, but its influence over the world's fate is undeniable. As they move toward the glade, tensions simmer beneath the surface—the Forest's whispers grow urgent, the mountains rumble with impatience, and the Kingdom's veneer of order strains under the weight of the moment. The next steps will determine whether this fragile alliance holds or shatters entirely.

#### ===== Mountain Chieftain's Round =====

```
<action> Grimrock grunts, shifting his weight as he adjusts the grip on his battle-axe. His dark eyes flick between Eldara’s glowing staff and Thorn’s pulsing green light, the fire in his scars simmering with impatience.</action>

<think> *Bah! More talk of purity and silence. If the artifact’s half as clever as they claim, it’ll know a dwarf’s worth by the weight of his axe and the strength of his arm.* </think>   

<speak> "Aye, we’ll go together—no blades, no spells, fine. But mark this, elf: if that trinket’s got half the sense of a dwarven forge, it’ll see the value in honest labor over pretty words." </speak>

<action> He takes a heavy step forward, his spiked helmet glinting as he shoulders past a low-hanging branch. The wine pot at his waist sloshes with each determined stride.</action>       

<speak> "And Thorn—yer ‘earth remembers every step’? Pfah! The mountains remember the dwarves who carve ‘em, not the wind that whispers over ‘em. Let’s see what this artifact’s made of." </speak>

<think> *If it’s treasure, it’s ours. If it’s trouble, we’ll cage it. And if it’s got a mind of its own... well, we’ll see whose will is stronger.* </think>

<action> He spares one last glance at the others, his grin fierce beneath his beard. "Well? Keep up, or are ye both waitin’ for an invitation?"</action>
```

#### ===== Round 9 World State =====

The representatives of the Forest, the Tribe, and the Kingdom have reached a tense agreement to approach the artifact together, each bound by their own convictions but united in purpose. Thorn's connection to nature warns of impending imbalance, Grimrock's dwarven pride demands action, and Eldara's diplomatic wisdom seeks to mediate. As they move toward the glade where the artifact rests, the air grows thick with unspoken tension—the Forest's whispers grow urgent, the mountains rumble with impatience, and the Kingdom's veneer of order strains under the weight of the moment. The artifact's true nature remains unknown, but its influence over the world's fate is undeniable. The next steps will determine whether this fragile alliance holds or shatters entirely.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's lips press into a thin line as Grimrock strides ahead, her grip on her staff tightening imperceptibly. The crystal's glow dims slightly, as if mirroring her restrained frustration.</action>

<think> His bravado is a hammer in search of a nail—crude, but effective. Yet even the sturdiest hammer shatters against the wrong anvil. If the artifact rejects him, will his pride allow him to accept it? Or will he force a conflict that could unravel centuries of fragile peace?</think>

<speak> "Patience, Grimrock. The artifact has waited this long; it will not vanish for the sake of a few more measured steps."</speak>

<action> She glides forward, her robes whispering over the grass, her staff's light casting long shadows ahead. Her gaze flicks to Thorn, noting the way the Forest shaman's eyes remain fixed on the rustling leaves.</action>

<think> Thorn's faith in nature's judgment is admirable, but the world is not so simple. Magic items may choose, but mortals interpret—and misinterpret. If the artifact's choice divides us further, will he stand by his ideals, or will the Forest's whispers demand something darker?</think>

<speak> "Thorn, you speak of balance. If the artifact's answer is... unexpected, will the Forest abide by it? Or will the winds carry new warnings?"</speak>

<action> She pauses at the edge of the glade, the artifact's resting place now visible—a shimmering, indistinct shape hovering above a stone pedestal, pulsing with latent power. Her breath catches, just for a moment.</action>

<think> So this is the thread that could unravel us all. Let it see the Kingdom's wisdom. Let it choose peace.</think>

<speak> "We stand at the threshold. Let us approach together—and may the world's balance guide us."</speak>
```

#### ===== Round 10 World State =====

The representatives of the Forest, the Tribe, and the Kingdom stand at the edge of the glade, the artifact pulsing with latent power before them. Thorn's connection to nature hums with unease, Grimrock's dwarven pride bristles at the delay, and Eldara's diplomatic resolve strains under the weight of the moment. The artifact's presence is undeniable—its choice, or lack thereof, will determine whether this fragile alliance holds or shatters. The air is thick with tension, each faction's values and desires laid bare as they prepare to face the artifact's judgment together.

#### ===== Forest Shaman's Round =====

```
<think> The artifact hums with a power that resonates deep within the Forest's bones. Grimrock's impatience is a storm cloud, Eldara's caution a still pond—both necessary, yet neither seeing the full truth. The balance teeters... but perhaps this is the moment the world has been waiting for.</think>

<action> Thorn steps forward, his bare feet pressing into the earth as if drawing strength from it. The green light in his staff flares briefly, casting eerie shadows across his scarred face. His braids sway as he tilts his head, listening to the whispers of the wind through the leaves.</action>

<speak> "The Forest does not fear the unexpected, Eldara. It adapts, as all living things must. But heed this—the artifact's answer may not be a choice between us, but a challenge for us all."</speak>

<action> He raises his staff, the carvings along its length glowing faintly as he gestures toward the shimmering artifact. The charms in his hair clink softly, stirred by an unseen breeze.</action>

<speak> "Grimrock, your strength is undeniable. Eldara, your wisdom is vast. But the artifact will not judge us by what we wield or what we know—it will judge us by what we are willing to surrender. Are you prepared to lay down your axes and your spells, if the balance demands it?"</speak>

<think> The air is thick with tension, like the moment before lightning strikes. The Forest holds its breath... and so must I.</think>

<action> Thorn takes a slow, deliberate step toward the glade, his staff's light pulsing in time with the artifact's rhythm. His voice drops to a murmur, barely louder than the rustling leaves.</action>

<speak> "Come. Let us face the answer together—whatever it may be."</speak>
```

#### ===== Round 11 World State =====

The representatives of the Forest, the Tribe, and the Kingdom stand at the edge of the glade, the artifact pulsing with latent power before them. Thorn's connection to nature hums with unease, Grimrock's dwarven pride bristles at the delay, and Eldara's diplomatic resolve strains under the weight of the moment. The artifact's presence is undeniable—its choice, or lack thereof, will determine whether this fragile alliance holds or shatters. The air is thick with tension, each faction's values and desires laid bare as they prepare to face the artifact's judgment together. The artifact hovers above a stone pedestal, its shimmering form resonating with the trio's conflicting energies—Thorn's green magic, Eldara's azure glow, and Grimrock's fiery determination. The moment of reckoning is near.

#### ===== Mountain Chieftain's Round =====

```
<action> Grimrock rolls his broad shoulders, the spikes on his helmet catching the light as he steps forward, his battle-axe resting easily against his shoulder. His dark eyes gleam with a mix of defiance and curiosity as he studies the shimmering artifact.</action>

<think> *Surrender? Pfah! A dwarf surrenders nothing but sweat and steel. But if this trinket wants a test, then let it see the mettle of the Mountain Tribe.* </think>

<speak> "Lay down me axe? Not likely, Thorn. But if this artifact’s got a challenge, then let it speak plain. I’ll not dance around its riddles like some elf at court!" </speak>

<action> He strides toward the pedestal, his boots thudding against the earth with each step. The wine pot at his waist sways, and he absently pats it, as if drawing courage from its weight.</action>

<speak> "Ye want unity? Fine. But mark me—if this thing’s got a lick of sense, it’ll see the value in a dwarf’s word. We don’t twist ours like silver-tongued elves or whisper like tree-folk. We say what we mean, and we mean what we say." </speak>

<action> He stops just short of the artifact, his shield raised slightly, not in threat but in readiness. The fire in his scars pulses faintly, as if in tune with the artifact’s glow.</action>

<think> *Let it choose. Let it try. The mountains don’t bend, and neither do we.* </think>

<speak> "Well? What’s it waitin’ for? A formal invitation?" </speak>

<action> He glares at the artifact, his beard bristling, as if daring it to make its move.</action>
```

#### ===== Round 12 World State =====

The artifact pulses with increasing intensity as the three representatives stand before it, their conflicting energies—Thorn's green magic, Eldara's azure glow, and Grimrock's fiery determination—intertwining in the air. The tension is palpable, each faction's values and desires laid bare. The artifact's judgment seems imminent, its choice—or rejection—poised to either solidify the fragile alliance or shatter it entirely. The winds have stilled, the Forest holds its breath, and the very earth beneath them seems to wait in anticipation.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's fingers tighten around her staff, the crystal's glow steadying as she watches Grimrock's bold approach. Her melancholic blue eyes flicker with a mix of caution and resolve, her silver hair catching the faint light of the artifact.</action>

<think> Grimrock's defiance is as unyielding as the mountains he hails from, but his bluntness may yet be his undoing. Thorn's faith in the artifact's judgment is noble, but the world is not so kind as to reward idealism alone. The Kingdom's stability hangs in the balance—I must ensure it is not tipped by recklessness.</think>

<speak> "Grimrock, your honesty is... refreshing, but even the sturdiest stone cracks under the weight of arrogance. Thorn, your trust in the artifact's wisdom is commendable, but wisdom often wears many faces."</speak>

<action> She steps forward, her azure robes flowing like a quiet river, and raises her staff slightly. The crystal's light casts a soft glow over the artifact, as if testing its nature.</action>

<speak> "Let us not provoke what we do not understand. If the artifact seeks a challenge, let it be one of unity, not dominance. The Kingdom stands for order, but order without harmony is brittle."</speak>

<think> The king would counsel patience, but patience wears thin when axes are raised and tempers flare. If the artifact chooses Grimrock, will Thorn accept it? If it chooses Thorn, will Grimrock honor his word? And if it chooses me... will they see it as wisdom or manipulation?</think>

<action> She turns her gaze fully to the artifact, her voice low but carrying the weight of centuries.</action>

<speak> "Artifact, if you will judge us, then judge us not by our words alone, but by the futures we would weave. The Kingdom seeks stability, the Forest seeks balance, and the Tribe seeks strength. Which thread will you choose to pull?"</speak>

<action> The crystal atop her staff pulses once, as if in silent agreement, and she waits, her breath steady, her eyes unblinking.</action>
```

#### ===== Round 13 World State =====

The artifact's glow intensifies, its pulsing light now synchronizing with the energies of the three representatives—Thorn's green magic, Eldara's azure glow, and Grimrock's fiery determination. The air crackles with tension as the artifact seems to weigh their words and intentions. The Forest's whispers grow silent, the mountains' echoes still, and even the Kingdom's order feels suspended in this pivotal moment. The artifact's judgment is imminent, poised to either unite or fracture the fragile alliance between the factions.

#### ===== Forest Shaman's Round =====

```
<think> The artifact pulses with a rhythm that echoes the heartbeat of the Forest itself. Grimrock's defiance is like a wildfire—uncontrolled but full of life. Eldara's measured words are the cool waters that seek to temper it. Yet neither sees the deeper truth: the artifact is not just a judge, but a mirror. It reflects the fractures between us, and the choice it offers may be one we cannot foresee.</think>

<action> Thorn closes his eyes, drawing in a slow breath as the green light in his staff flickers like a dying ember. The charms in his braids tremble, stirred by the unseen currents of magic swirling around the artifact. When he opens his eyes again, the sparks within them burn brighter, reflecting the artifact's glow.</action>

<speak> "Grimrock, your honesty is the mountain's roar—loud, unyielding. Eldara, your wisdom is the river's flow—deep, unwavering. But the artifact does not seek to crown one over the other. It seeks... alignment."</speak>

<action> He steps forward, his bare feet pressing into the earth as if rooting himself to the world's pulse. His staff rises, the carvings along its length glowing faintly as he points it toward the artifact. The air hums with energy, the Forest's whispers growing urgent.</action>

<speak> "Look closer. It does not judge us as individuals, but as fragments of a greater whole. The Kingdom's order, the Tribe's strength, the Forest's balance—these are not opposing forces. They are threads of the same tapestry."</speak>

<think> The artifact's light shifts, its glow now tinged with gold, green, and azure—colors of the three factions. It is not choosing. It is weaving. And if we do not see it, the unraveling will be swift.</think>

<action> Thorn's voice drops to a whisper, barely audible over the rustling leaves. His gaze locks onto the artifact, his expression unreadable but his eyes alight with understanding.</action>

<speak> "It is not waiting for us to prove ourselves. It is waiting for us to remember—we are already bound. The question is not which thread it will pull, but whether we will let it weave us together... or tear us apart."</speak>

<action> He lowers his staff, the green light dimming as if in deference to the artifact's growing radiance. The wind stills, the Forest holds its breath, and for a moment, the world itself seems to pause.</action>

<speak> "The choice is yours. But choose quickly—the storm gathers."</speak>
```

#### ===== Round 14 World State =====

The artifact's glow shifts, now shimmering with gold, green, and azure—colors representing the Kingdom, the Forest, and the Tribe. Its pulsing light weaves through the air, binding the three representatives in a visible tapestry of energy. The tension is palpable as the artifact's intent becomes clear: it seeks not to choose one over the others, but to unite them. The Forest's whispers, the mountains' echoes, and the Kingdom's order all resonate in harmony, awaiting the final decision that will either forge an alliance or fracture the fragile peace.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's gaze lingers on the artifact, her melancholic blue eyes reflecting its shimmering light. The crystal atop her staff pulses in harmony with the artifact's rhythm, as if whispering secrets only she can hear.</action>

<think> Thorn speaks of unity, yet his words carry the weight of the Forest's isolation. Grimrock's defiance is a blade poised to cut the very threads we seek to weave. The artifact's glow... it does not favor one over the other. It seeks something deeper—something the Kingdom has long understood: order is meaningless without harmony.</think>

<speak> "Thorn, your insight is... illuminating. Grimrock, your strength is undeniable. But the artifact's radiance does not dim for one and brighten for another. It shines for all—or none."</speak>

<action> She steps forward, her azure robes flowing like a quiet tide, and extends her staff toward the artifact. The crystal's light intertwines with the artifact's glow, casting intricate patterns across the glade.</action>

<speak> "The Kingdom proposes this: let the artifact not choose a keeper, but a purpose. Let it guide us not as rivals, but as stewards. If it seeks alignment, then let us align—not under one banner, but as three pillars upholding the same sky."</speak>

<think> The king would approve. A shared burden, not a contested prize. If Thorn's Forest and Grimrock's Tribe can accept this, the peace may yet hold. If not... then the artifact's judgment will be the least of our concerns.</think>

<action> She turns her gaze to Grimrock, then Thorn, her voice softening but losing none of its authority.</action>

<speak> "Will the Tribe and the Forest stand with the Kingdom in this? Or will we let pride fracture what magic seeks to unite?"</speak>

<action> The crystal atop her staff flares once, a silent challenge—or perhaps an offering.</action>
```

#### ===== Round 15 World State =====

The artifact's glow shifts, now shimmering with gold, green, and azure—colors representing the Kingdom, the Forest, and the Tribe. Its pulsing light weaves through the air, binding the three representatives in a visible tapestry of energy. The tension is palpable as the artifact's intent becomes clear: it seeks not to choose one over the others, but to unite them. The Forest's whispers, the mountains' echoes, and the Kingdom's order all resonate in harmony, awaiting the final decision that will either forge an alliance or fracture the fragile peace.

#### ===== Mountain Chieftain's Round =====

```
<action> Grimrock's thick fingers drum against the haft of his battle-axe, the rhythmic thud echoing like a forge hammer. His dark eyes narrow as he watches the artifact's glow mingle with Eldara's crystal, the colors swirling like molten metal in a crucible.</action>

<think> *Three pillars, eh? Sounds like elf-talk for "let's all hold hands and sing." But... if this thing's power is real, and it's not just some shiny lure for fools...* </think>        

<speak> "Aye, elf, yer words are pretty as polished silver. But the Tribe doesn’t uphold the sky—we carve our own path through it!" </speak>

<action> He spits to the side, then hefts his axe, turning the blade so it catches the artifact’s light. The fire in his scars flares briefly, as if in challenge.</action>

<think> *Thorn’s right about one thing—this ain’t about crowns or caging. But strength’s still the answer. Just not the kind they’re thinkin’.* </think>

<speak> "Fine. If the artifact wants unity, then let’s show it what that means—dwarf-style. No singin’, no whisperin’, just honest labor. We’ll forge a pact, right here, with steel and stone as witnesses!" </speak>

<action> He slams his axe into the ground, the impact sending a tremor through the glade. With his free hand, he yanks the wine pot from his belt and takes a deep swig, then offers it first to Thorn, then Eldara, his grin fierce beneath his beard.</action>

<speak> "A drink to seal the deal. Or are ye both too dainty for dwarven ale?" </speak>

<think> *Let’s see if their fancy magic can stomach a taste of the mountains.* </think>
```

#### ===== Round 16 World State =====

The artifact's glow shifts, now shimmering with gold, green, and azure—colors representing the Kingdom, the Forest, and the Tribe. Its pulsing light weaves through the air, binding the three representatives in a visible tapestry of energy. The tension is palpable as the artifact's intent becomes clear: it seeks not to choose one over the others, but to unite them. The Forest's whispers, the mountains' echoes, and the Kingdom's order all resonate in harmony, awaiting the final decision that will either forge an alliance or fracture the fragile peace. Grimrock's offer of a dwarven pact, sealed with ale, hangs in the air—a test of unity in the face of tradition and pride.

#### ===== Royal Advisor's Round =====

```
<action> Eldara's lips twitch slightly at Grimrock's offer, her melancholic blue eyes flickering with a mix of amusement and exasperation. She watches the dwarven ale slosh in the pot, its pungent aroma wafting through the glade.</action>

<think> A dwarven pact sealed with ale—crude, but undeniably sincere. The king would chuckle at the simplicity, though he'd never admit it. Still, if this is what it takes to bind the Tribe's word... </think>

<speak> "Grimrock, your ale is as unrefined as your diplomacy, but the gesture is... appreciated." </speak>

<action> She reaches out, her slender fingers wrapping around the wine pot with deliberate grace. She takes a measured sip, her expression unreadable as the strong brew burns its way down. The crystal atop her staff flickers briefly, as if in protest.</action>

<speak> "The Kingdom accepts your pact. Let steel and stone witness it—and let the artifact see our unity, however unorthodox its sealing." </speak>

<action> She passes the pot to Thorn, her gaze lingering on the artifact's pulsing light. The azure glow of her staff intertwines with its radiance, casting shimmering reflections across her silver hair.</action>

<think> If this is the thread that binds us, then let it hold. The king's peace depends on it—and so does the world's balance. </think>

<speak> "Thorn, the Forest's voice is yours to answer. Will you drink to this alliance, or will the winds carry your refusal?" </speak>

<action> She steps back, her staff's light steadying, her posture regal yet open—a silent challenge and an offering in one.</action>
```

#### ===== Round 17 World State =====

The artifact's glow shifts, now shimmering with gold, green, and azure—colors representing the Kingdom, the Forest, and the Tribe. Its pulsing light weaves through the air, binding the three representatives in a visible tapestry of energy. The tension is palpable as the artifact's intent becomes clear: it seeks not to choose one over the others, but to unite them. The Forest's whispers, the mountains' echoes, and the Kingdom's order all resonate in harmony, awaiting the final decision that will either forge an alliance or fracture the fragile peace. Grimrock's offer of a dwarven pact, sealed with ale, hangs in the air—a test of unity in the face of tradition and pride. Thorn now holds the wine pot, the Forest's response pivotal to the artifact's judgment.

#### ===== Forest Shaman's Round =====

```
<think> Grimrock's ale is as rough as his tongue, and Eldara's sip was a dance of diplomacy. But the Forest does not judge by refinement—it judges by truth. The artifact's light weaves our colors together, and the winds whisper of a path forward. Balance demands sacrifice, but also trust.</think>

<action> Thorn takes the wine pot from Eldara, his calloused fingers wrapping around its worn surface. He studies the dark liquid within, the green sparks in his eyes reflecting like fireflies in a deep pool. The charms in his braids clink softly as he tilts his head, listening to the distant rustle of leaves.</action>

<speak> "The Forest does not drink often, Grimrock... but it remembers the taste of rain, the strength of roots, and the fire of the sun. This ale of yours—it carries the mountain's breath, does it not?" </speak>

<action> He raises the pot to his lips and takes a slow, deliberate swallow, his throat working as the ale burns its way down. When he lowers it, his exhale is sharp, but his lips curl into a rare, faint smile.</action>

<speak> "A strong brew, for strong bonds. The Forest accepts your pact—sealed not by steel or stone alone, but by the earth that cradles us all." </speak>

<action> He passes the pot back to Grimrock, then turns to the artifact, his staff pulsing softly in time with its glow. The green light flares briefly as he plants it into the ground, the carvings along its length shimmering like veins of emerald.</action>

<speak> "Now, let the artifact see what we have woven. Let it answer not to one hand, but to three hearts—aligned, if not yet united." </speak>

<think> The storm gathers, but so does the dawn. The Forest's whispers grow quiet, waiting. Whatever comes next... we face it together.</think>
```

#### ===== Round 18 World State =====

The artifact's glow intensifies, its gold, green, and azure light merging into a radiant harmony as the pact is sealed. The air hums with latent power, the artifact resonating with the unity of the three representatives. The Forest's whispers quiet, the mountains' echoes still, and the Kingdom's order holds its breath—all awaiting the artifact's final judgment. The tension shifts from rivalry to anticipation, as the artifact's purpose now seems clear: it seeks not a keeper, but a covenant. The world's balance trembles on the edge of revelation.

#### ===== Royal Advisor's Round =====

```
<action> Eldara watches as Thorn drinks from the dwarven ale, her expression unreadable but her posture relaxed. The crystal atop her staff dims slightly, as if mirroring her cautious optimism.</action>

<think> Grimrock's ale is as rough as his tongue, yet there is a sincerity in this gesture that treaties and councils often lack. Thorn's acceptance is a hopeful sign—perhaps the Forest's whispers are not so opposed to unity after all. The artifact's glow... it brightens as we stand together. Is this the alignment it seeks?</think>

<speak> "Then let it be done. The Kingdom, the Forest, and the Tribe stand as one before the artifact. Let it witness our pact—not of conquest, but of shared stewardship."</speak>

<action> She raises her staff, the crystal's light merging with the artifact's radiance, casting a shimmering tapestry of gold, green, and azure across the glade. Her voice carries the weight of centuries, yet there is a rare warmth beneath its measured tone.</action>

<speak> "Grimrock, your ale has sealed more than a bargain—it has bridged divides older than these trees. Thorn, your faith in the earth's wisdom has guided us well. Now, let the artifact speak its truth."</speak>

<think> If it chooses none of us, the peace may hold. If it chooses one... then the others must honor their word. The king's laws demand it, and so does the world's balance.</think>       

<action> She steps forward, her azure robes flowing like a quiet river, and extends her free hand toward the artifact, palm open in offering. Her blue eyes reflect its pulsing light, unwavering.</action>

<speak> "We are ready."</speak>
```

#### ===== Round 19 World State =====

The artifact's glow intensifies, its gold, green, and azure light merging into a radiant harmony as the pact is sealed. The air hums with latent power, the artifact resonating with the unity of the three representatives. The Forest's whispers quiet, the mountains' echoes still, and the Kingdom's order holds its breath—all awaiting the artifact's final judgment. The tension shifts from rivalry to anticipation, as the artifact's purpose now seems clear: it seeks not a keeper, but a covenant. The world's balance trembles on the edge of revelation.

#### ===== Forest Shaman's Round =====

```
<think> The artifact's glow is no longer just light—it is a living thing, breathing in time with the world's pulse. Grimrock's ale sits warm in my belly, a reminder of the fire he carries. Eldara's crystal hums with quiet power, a counterpoint to the Forest's whispers. The pact is sealed, but the true test begins now.</think>

<action> Thorn steps forward, his bare feet pressing into the earth as if drawing strength from its depths. The green light in his staff flares, then steadies, mirroring the artifact's rhythm. His braids sway as he tilts his head, listening to the silence between heartbeats.</action>

<speak> "The Forest hears you, artifact. It has always heard. But now, we listen together—Kingdom, Tribe, and Forest. Speak, and we will heed."</speak>

<action> He reaches out, not with his staff, but with his free hand, palm upturned like Eldara's. The scars on his skin catch the artifact's light, old wounds that have long since healed but never faded. The charms in his hair tremble, stirred by the unseen currents of magic.</action>

<think> It is not just choosing. It is remembering. And so must we.</think>

<speak> "Grimrock, your axe is your truth. Eldara, your crystal is your wisdom. My staff is my bond to the earth. Let the artifact see them all—not as weapons, but as offerings. Let it decide what to make of us."</speak>

<action> The wind rises, rustling the leaves like a thousand hushed voices. The artifact's glow intensifies, its light weaving around their outstretched hands, their weapons, their symbols of power. Thorn's breath catches, but he does not flinch.</action>

<speak> "Steady now. The storm comes... but so does the dawn."</speak>
```

### Final Story

```markdown
**The Pact of the Artifact**  

The ancient Forest murmured with unrest, its leaves rustling warnings on the wind. Thorn, the Forest Shaman, stepped from the shadows of the oaks, his twisted staff pulsing with green light. His braided hair, adorned with feathers and charms, swayed as he listened to the whispers of the trees.

*The artifact stirs,* he thought. *It does not belong to any one faction—not the Kingdom, the Tribe, nor the Forest. It is a test of unity.*

Grimrock, the dwarven chieftain, stood like a mountain himself, his spiked helmet glinting as he stroked his thick beard. His battle-axe rested against his shoulder, and his dark eyes burned with impatience.

"Bah! If this magic trinket’s dangerous, the Tribe will forge a cage for it!" he boomed, taking a swig from his wine pot. "And if it’s treasure, then by stone and sweat, it’s ours to claim!"

Eldara, the high elf advisor, stood serene in her azure robes, her crystal-topped staff glowing faintly. Her silver hair shimmered as she spoke with measured wisdom. "This artifact is no mere prize. It is a thread in the world’s tapestry. The Kingdom proposes a council—let us study it before acting in haste."

Thorn’s eyes flickered with green sparks. "The Forest does not whisper idly. This artifact is alive—it will choose its own keeper, if we let it."

Grimrock scoffed. "Then let’s go to the damned thing and see whose will is stronger!"

Eldara exhaled softly. "Very well. We approach together—no blades, no spells. Let it judge our intentions."

The artifact hovered above a stone pedestal, its light shifting between gold, green, and azure—colors of the three factions. The air hummed with latent power.

Thorn pressed a hand to the earth, feeling its tremor. "It does not seek a victor. It seeks alignment."

Grimrock stepped forward, his axe planted firmly. "Then let it see dwarven steel!"

Eldara raised her staff. "Or elven wisdom."

Thorn’s voice was low. "Or the Forest’s balance."

The artifact pulsed brighter, its light weaving around them.

Eldara spoke first. "Let it choose not a keeper, but a purpose. Let us stand as three pillars—Kingdom, Tribe, and Forest—upholding the same sky."

Grimrock grunted, then yanked his wine pot free. "Aye, then let’s seal this pact dwarf-style!" He drank deeply, then offered it to Eldara.

She sipped with grace, though her crystal flickered in protest. "The Kingdom accepts."

Thorn took the pot next, the ale burning like mountain fire. "The Forest accepts."

As the last drop was drunk, the artifact’s glow intensified, its light merging into radiant harmony. The winds stilled. The earth held its breath.

Then, in a voice like rustling leaves and echoing stone, the artifact spoke:

*"Unity is not taken. It is given."*

The light flared—gold, green, and azure entwined—and then settled, not upon one, but upon all three.

Thorn smiled faintly. "The balance is kept."

Grimrock clapped his hands. "Then let’s get to work!"

Eldara nodded. "For the world’s sake."

And so, beneath the artifact’s watchful glow, the pact was sealed—not by force, but by choice.

The storm had passed.

The dawn had come.
```

## Acknowledgements

- This tiny toy project is inspired by the work of [BookWorld](https://arxiv.org/pdf/2504.14538).