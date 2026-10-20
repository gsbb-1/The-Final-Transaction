-- Strip the "Chapter N: " prefix from level-1 headings.
--
-- Every chapter file opens with "# Chapter N: Title" (see the manuscript
-- conventions in AGENTS.md). LaTeX's \chapter already prints "Chapter N" and
-- numbers itself, so leaving the prefix in would print
--
--     Chapter 1
--     Chapter 1: Life lesson
--
-- This filter drops "Chapter N:" and keeps the title, so the opener reads
--
--     Chapter 1
--     Life lesson
--
-- The manuscript's chapter numbers run 1..55 in file order, so LaTeX's own
-- numbering matches the author's.

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local inlines = el.content

  -- The prefix parses as Str "Chapter", Space, Str "N:", Space.
  local cut = nil
  for i, e in ipairs(inlines) do
    if e.t == "Str" and e.text:match("^%d+:%s*$") then
      cut = i
      break
    end
  end
  if not cut then
    return nil
  end

  local kept = {}
  local seen_text = false
  for i = cut + 1, #inlines do
    if inlines[i].t ~= "Space" or seen_text then
      kept[#kept + 1] = inlines[i]
      seen_text = true
    end
  end

  el.content = pandoc.Inlines(kept)
  return el
end
