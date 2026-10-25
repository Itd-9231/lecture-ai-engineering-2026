# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：
　固有の文脈に沿った回答ではなく、一般論を展開している

- 用語集の正しい意味と比べて気づいたこと：
  glossary.jsonにあった文章は以下の通りであった。
   {
      "id": "lora",
      "term": "LoRA",
      "aliases": ["Low-Rank Adaptation"],
      "lecture": 2,
      "category": "ファインチューニング",
      "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラメータが少なく、学習結果（アダプタ）も小さいファイルで保存できる。本講座の第2回演習ではLoRAを扱う。",
      "related": ["peft", "lora-rank", "qlora"]
    },

    上記のdefinitionにある「行列」という用語は、gemini-3.5-flash-lite、gemini-3.5-flash、gemini-3.8-flashのうち、gemini-3.8-flashだけに登場しており、gemini-3.5-flash-liteとgemini-3.5-flashでは登場していない。このことは、回答はわかりやすさを優先し、学術的な説明をできるだけ省略したものであると考えられる。

- 表示できたトークン数（入力 / 出力）：
　[model] gemini-3.5-flash-lite: [usage] input_tokens=7 output_tokens=632
　[model] gemini-3.5-flash: [usage] input_tokens=7 output_tokens=620
　[model] gemini-3.8-flash: [usage] input_tokens=7 output_tokens=804

## 宿題

- 取り組んだレベル：基礎

- やったこと：AIEモデル３種類で回答を比較した

- 結果：
　・[model] gemini-3.5-flash-lite: [usage] input_tokens=7 output_tokens=632
　　1. なぜLoRAが必要なのか？（背景）
　　2. LoRAの仕組み
　　3. LoRAのすごいメリット
　　まとめ
　・[model] gemini-3.5-flash: [usage] input_tokens=7 output_tokens=620
　　LoRAのわかりやすいイメージ（例え話）
　　LoRAの主なメリット
　　主な活用例
　　まとめ
　・[model] gemini-3.8-flash: [usage] input_tokens=7 output_tokens=804
　　なぜLoRAが必要なのか？（背景）
　　LoRAの仕組み（わかりやすい例え）
　　LoRAのメリット
　　主な活用例
　　まとめ

- 気づき・疑問：
　・gemini-3.5-flash-liteやgemini-3.5-flashと比較して、gemini-3.8-flashはtoken数も格段に増加している
　　見出しを比較すると、gemini-3.5-flash-liteの回答には「背景」があるが「例え」がなく、またgemini-3.5-flashの回答には「例え」があるが「背景」
　　はない。一方、gemini-3.8-flashでは「背景」と「例え」を両方とも包含しており、内容が一層充実していることがわかった
　・回答を得るまでの体感時間は、AIEモデルのスペックが上がるにつれて、処理時間も長くなっていると感じた

以上
